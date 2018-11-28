import json
import web3
from web3 import Web3
from solc import compile_source
from web3.contract import ConciseContract

def getw3():
  #target = 'http://172.13.0.2:8545'
  target = 'http://127.0.0.1:8545'
  aprovider = Web3.HTTPProvider(target)
  w3 = Web3(aprovider)
  assert w3.isConnected(), 'node not connected at {}'.format(target)
  return w3

w3 = getw3()

contract_source_code = '''
pragma solidity ^0.4.21;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        return greeting;
    }
}
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']


# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]



# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()


# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'],
)
print('Contract deployed address [{}]'.format(tx_receipt.contractAddress))

# Display the default greeting from the contract
print('Default contract greeting: {}'.format(
    greeter.functions.greet().call()
))

print('Setting the greeting to WelcomeHelloWorld...')
tx_hash = greeter.functions.setGreeting('WelcomeHelloWorld').transact()

# Wait for transaction to be mined...
w3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting value
print('Updated contract greeting: {}'.format(
    greeter.functions.greet().call()
))

# When issuing a lot of reads, try this more concise reader:
reader = ConciseContract(greeter)
assert reader.greet() == "WelcomeHelloWorld"


