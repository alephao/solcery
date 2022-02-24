import errors

def test_gen_error_entry():
    test_cases = [
        ({ "name": "Foo", "args": [] }, 'function Foo() internal returns (bytes memory) { return abi.encodeWithSignature(\"Foo()\"); }'),
        ({ "name": "Foo", "args": [{ "type": "uint256", "name": "a" }] }, 'function Foo(uint256 a) internal returns (bytes memory) { return abi.encodeWithSignature(\"Foo(uint256)\", a); }'),
        ({ "name": "Foo", "args": [{ "type": "uint256", "name": "" }] }, 'function Foo(uint256 p1) internal returns (bytes memory) { return abi.encodeWithSignature(\"Foo(uint256)\", p1); }'),
        ({ "name": "Foo", "args": [{ "type": "uint256", "name": "a" }, { "type": "uint256", "name": "b" }] }, 'function Foo(uint256 a, uint256 b) internal returns (bytes memory) { return abi.encodeWithSignature(\"Foo(uint256,uint256)\", a, b); }'),
        ({ "name": "Foo", "args": [{ "type": "uint256", "name": "" }, { "type": "uint256", "name": "" }] }, 'function Foo(uint256 p1, uint256 p2) internal returns (bytes memory) { return abi.encodeWithSignature(\"Foo(uint256,uint256)\", p1, p2); }'),
    ]

    for tc in test_cases:
        input = tc[0]
        output = errors.gen_error_entry(input)
        expected = tc[1]
        assert output == expected, "{} != {}".format(output, expected)

def test_gen_functions():
    errs = [
      { "name": "Foo", "args": [] },
      { "name": "Bar", "args": [{ "type": "uint256", "name": "a" }] },
      { "name": "Baz", "args": [{ "type": "uint256", "name": "" }] },
      { "name": "Boo", "args": [{ "type": "uint256", "name": "a" }, { "type": "uint256", "name": "b" }] },
      { "name": "Far", "args": [{ "type": "uint256", "name": "" }, { "type": "uint256", "name": "" }] },
    ]

    expected = [
      "function Foo() internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Foo()\"); }",
      "function Bar(uint256 a) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Bar(uint256)\", a); }",
      "function Baz(uint256 p1) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Baz(uint256)\", p1); }",
      "function Boo(uint256 a, uint256 b) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Boo(uint256,uint256)\", a, b); }",
      "function Far(uint256 p1, uint256 p2) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Far(uint256,uint256)\", p1, p2); }",
    ]

    output = errors.gen_functions(errs)
    assert output == expected, "====\n{}\n!=\n{}\n====".format(output, expected)

def test_gen_file_contents():
    errs = [
      { "name": "Foo", "args": [] },
      { "name": "Bar", "args": [{ "type": "uint256", "name": "a" }] },
      { "name": "Baz", "args": [{ "type": "uint256", "name": "" }] },
      { "name": "Boo", "args": [{ "type": "uint256", "name": "a" }, { "type": "uint256", "name": "b" }] },
      { "name": "Far", "args": [{ "type": "uint256", "name": "" }, { "type": "uint256", "name": "" }] },
    ]

    expected = """// SPDX-License-Identifier: Unlicense
pragma solidity >=0.8.4;

// The code in this file was generate. Do not modify!
// solhint-disable const-name-snakecase
library Errors {
    function Foo() internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Foo()\"); }
    function Bar(uint256 a) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Bar(uint256)\", a); }
    function Baz(uint256 p1) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Baz(uint256)\", p1); }
    function Boo(uint256 a, uint256 b) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Boo(uint256,uint256)\", a, b); }
    function Far(uint256 p1, uint256 p2) internal pure returns (bytes memory) { return abi.encodeWithSignature(\"Far(uint256,uint256)\", p1, p2); }
}
// solhint-enalbe const-name-snakecase"""

    output = errors.gen_file_contents(errs)
    assert output == expected, "====\n{}\n!=\n{}\n====".format(output, expected)


if __name__ == "__main__":
    test_gen_error_entry()
    test_gen_functions()
    test_gen_file_contents()
    print("All tests passed!")
