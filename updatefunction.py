import json
import web3
from web3 import Web3

def getw3():
  #target = 'http://172.13.0.2:8545'
  target = 'http://127.0.0.1:8545'
  aprovider = Web3.HTTPProvider(target)
  w3 = Web3(aprovider)
  assert w3.isConnected(), 'node not connected at {}'.format(target)
  return w3

w3 = getw3()

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Create the contract instance with the newly-deployed address
address_deployed_contract = '0xD7b426cAB920eD78342261160136236Aa0C09ecB'

from contracts.packer import *
def donow():
  packer = Packer(w3, 'Greeter', 'contracts/greeter.sol')
  deployed = packer.from_deployed_instance(address_deployed_contract)
  reader = packer.get_concise_instance(address_deployed_contract)

  packer.update_function(deployed, 'setGreeting', 'more-wowow')

  print('11 [{}]'.format(deployed.functions.greet().call()))
  print('22 [{}]'.format(reader.greet()))


donow()

