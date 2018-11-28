import json
import web3
from web3 import Web3
from contracts.packer import *

address_deployed_contract = '0xbDaAe5285BEE72Ac7DEfaD987A8d67C36cde612f'

def getw3():
  #target = 'http://172.13.0.2:8545'
  target = 'http://127.0.0.1:8545'
  aprovider = Web3.HTTPProvider(target)
  w3 = Web3(aprovider)
  assert w3.isConnected(), 'node not connected at {}'.format(target)
  return w3


def getPacker():
  w3 = getw3()
  packer = Packer(w3, 'SimpleCounter', 'contracts/simplecounter.sol')
  return (w3, packer)

def deployibit():
  w3, packer = getPacker()
  deployed = packer.deploy_now(w3.eth.accounts[0])
  #reader = packer.get_concise_instance(deployed)

  print('11 [{}]'.format(deployed.functions.getBalance().call()))
  # print('12 [{}]'.format(reader.getBalance()))

def checkibit():
  w3, packer = getPacker()
  deployed = packer.from_deployed_instance(address_deployed_contract)
  reader = packer.get_concise_instance(address_deployed_contract)

  print('61 [{}]'.format(deployed.functions.getBalance().call()))
  print('62 [{}]'.format(reader.getBalance()))

def updateibit(params):
  w3, packer = getPacker()
  deployed = packer.from_deployed_instance(address_deployed_contract)
  reader = packer.get_concise_instance(address_deployed_contract)

  # params = (3200,)
  # print('params:', params)
  # packer.update_function(deployed, 'createNote', params[0], params[1])

  w3.eth.defaultAccount = w3.eth.accounts[0]
  txhash = deployed.functions.update(params[0])
  txhash = txhash.transact()
  w3.eth.waitForTransactionReceipt(txhash)

  print('81 [{}]'.format(deployed.functions.getBalance().call()))
  print('82 [{}]'.format(reader.getBalance()))


#deployibit()
checkibit()
updateibit( (323,) )

