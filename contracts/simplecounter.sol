pragma solidity ^0.4.20;

contract SimpleCounter {
  address owner;
  uint256 balance;
  uint256 max = 10000;

  constructor() public {
    owner = msg.sender;
  }

  function capmax(uint256 amount) public {
    max = amount;
  }

  function update(uint256 amount) public {
    balance = amount <= max ? amount : balance;
  }

  function getBalance() public view returns(uint256) {
    return balance;
  }
}

