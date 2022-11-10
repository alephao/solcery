# Solcery

> WIP!

Codegen tool for Solidity development.

## Installing

`TBD`

If you want to try this out, clone the repo and run `python main.py`

## Commands

### `solcery errsig [<path_to_file>]`

Add error signature comments on top of each `error` declaration if it contains a `/// @dev 0x` comment on top of it.

**Example:**

Given the file `MyContract.sol`, running `solcery errsig MyContract.sol` will update the file adding the contents bellow:

```diff
contract MyContract {
-   /// @dev 0x
+   /// @dev 0xbfb4ebcf
    error Foo();
-   /// @dev 0x
+   /// @dev 0xdd448093
    error Bar(uint256 a);
}
```

### `solcery errgen <output_path> [<input_path>]`

Generates a solidity file containing sugar functions to use when expecting errors.

**Example:**

Given the file bellow `MyContract.sol` containing some error declarations, running `solcery errgen Errors.sol MyContract.sol` will generate the file `Errors.sol` you can find below.

**MyContract.sol**

```solidity
contract MyContract {
    error Foo();
    error Bar(uint256 a);
    // ...
}
```

**Errors.sol**

```solidity
// SPDX-License-Identifier: Unlicense
pragma solidity >=0.8.4;

// The code in this file was generate. Do not modify!
// solhint-disable const-name-snakecase
library Errors {
    function Foo() internal pure returns (bytes memory) { return abi.encodeWithSignature("Foo()"); }
    function Bar(uint256 a) internal pure returns (bytes memory) { return abi.encodeWithSignature("Bar(uint256)", a); }
}
// solhint-enable const-name-snakecase
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