pragma solidity ^0.4.21;

// import './SafeMath.sol';

contract Swapnote {
  // using SafeMath for uint256;
  address public owner;
  address public counterparty;
  uint256 public amount;

  event EventNoteCreated(address indexed party, address indexed counterparty, uint256 amount);
  event EventNoteRevised(address indexed party, address indexed counterparty, uint256 amount);
  event EventNotePaid(address indexed party, address indexed counterparty, uint256 amount);

  function Swapnote() public {
    owner = msg.sender;
    amount = 1234;
  }

  function createNote(uint256 _amount) public {
    // counterparty = _counterparty;
    amount = _amount;
    emit EventNoteCreated(
      owner,
      address(0), // _counterparty,
      _amount
    );
  }

  function reviseNote(address _counterparty, uint256 _amount) public {
    counterparty = _counterparty;
    amount = _amount;
    emit EventNoteRevised(
      owner,
      _counterparty,
      _amount
    );
  }

  // function noteOwner() view public returns(address) {
  //   return owner;
  // }

  // function noteCounterParty() view public returns(address) {
  //   return counterparty;
  // }

  function noteAmount() view public returns(uint256) {
    return amount;
  }
}

