import common


def test_encode_signature():
    test_cases = [
        ("Foo()", "0xbfb4ebcf"),
        ("Bar()", "0xb0a378b0"),
        ("SomeError()", "0x332e27d2"),
        ("SomeError(uint256)", "0xac47be21"),
        ("SomeError(address)", "0x578255cd"),
        ("SomeError(address,bytes32)", "0x10858944"),
    ]

    for tc in test_cases:
        input = tc[0]
        output = common.encode_signature(input)
        expected = tc[1]
        assert output == expected, "{} != {}".format(output, expected)


def test_error_sig_to_obj():
    test_cases = [
      ("Foo()", { "name": "Foo", "args": [] }),
      ("Foo( )", { "name": "Foo", "args": [] }),
      
      ("Foo(uint256)",            { "name": "Foo", "args": [{ "type": "uint256", "name": "" }] }),
      ("Foo(uint256,uint256)",    { "name": "Foo", "args": [{ "type": "uint256", "name": "" }, { "type": "uint256", "name": "" }] }),
      ("Foo(uint256, uint256)",   { "name": "Foo", "args": [{ "type": "uint256", "name": "" }, { "type": "uint256", "name": "" }] }),
      ("Foo(uint256 , uint256)",  { "name": "Foo", "args": [{ "type": "uint256", "name": "" }, { "type": "uint256", "name": "" }] }),

      ("Foo(uint256 a)",              { "name": "Foo", "args": [{ "type": "uint256", "name": "a" }] }),
      ("Foo(uint256 a, uint256 b)",   { "name": "Foo", "args": [{ "type": "uint256", "name": "a" }, { "type": "uint256", "name": "b" }] }),
      ("Foo(uint256 a , uint256 b)",  { "name": "Foo", "args": [{ "type": "uint256", "name": "a" }, { "type": "uint256", "name": "b" }] }),
      ("Foo(uint256 a,uint256 b)",    { "name": "Foo", "args": [{ "type": "uint256", "name": "a" }, { "type": "uint256", "name": "b" }] }),
    ]

    for tc in test_cases:
        input = tc[0]
        output = common.error_sig_to_obj(input)
        expected = tc[1]
        assert output == expected, "{} != {}".format(output, expected)


def test_errors_on_content():
    output = common.errors_on_content(
        """
  contract Hello {
    error Foo();
    error   Bar(uint256 a);

    func helloWorld()

    error Baz(address a, uint256 b);
  }
  """
    )
    
    expected = [
        "Foo()",
        "Bar(uint256 a)",
        "Baz(address a, uint256 b)",
    ]

    assert output == expected, "{} != {}".format(output, expected)


if __name__ == "__main__":
    test_encode_signature()
    test_error_sig_to_obj()
    test_errors_on_content()
    print("All tests passed!")
