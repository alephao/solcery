# Solcery

> WIP!

Codegen tool for Solidity development.

## Installing

`TBD`

If you want to try this out, clone the repo and run `main.py`

## Commands

### `solcery errgen <output_path> [<input_path>]`

Generates a solidity file containing sugar functions to use when expecting errors.

**Example input**:

```solidity
contract MyContract {
    error Foo();
    error Bar(uint256 a);
    // ...
}
```

**Example output**:

```solidity
// SPDX-License-Identifier: Unlicense
pragma solidity >=0.8.4;

// The code in this file was generate. Do not modify!
// solhint-disable const-name-snakecase
library Errors {
    function Foo() internal pure returns (bytes memory) { return abi.encodeWithSignature("Foo()"); }
    function Bar(uint256 a) internal pure returns (bytes memory) { return abi.encodeWithSignature("Bar(uint256)", a); }
}
// solhint-enalbe const-name-snakecase
```

**Usage in a foundry test file**:

```solidity
contract MyTests {
    function testSomething() public {
      HEVM.expectRevert(Errors.Bar(123))
      //...
    }
}
```