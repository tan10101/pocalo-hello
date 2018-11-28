import web3
from web3 import Web3
from solc import compile_source
from web3.contract import ConciseContract

class Packer():
  def __init__(self, w3, contract_name, filename):
    self.w3 = w3
    with open(filename) as f:
      solidity_source_code = f.read()
      compiled_sol = compile_source(solidity_source_code)
      contract_interface = compiled_sol['<stdin>:{}'.format(contract_name)]

      self.abi = contract_interface['abi']
      self.bytecode = contract_interface['bin']
      self.contract = w3.eth.contract(abi=self.abi, bytecode=self.bytecode)
      self.contract_name = contract_name

  def deploy_now(self, sender, *params):
    self.w3.eth.defaultAccount = sender
    # submit the transaction that deploys the contract
    txhash = self.contract.constructor(*params).transact()

    # wait for the transaction to be mined and get the transaction receipt
    txreceipt = self.w3.eth.waitForTransactionReceipt(txhash)
    deployed_address = txreceipt.contractAddress
    print('Contract [{}] is deployed at address [{}]'.format(self.contract_name, deployed_address))
    return self.from_deployed_instance(deployed_address)

  def from_deployed_instance(self, deployed_address):
    deployed = self.w3.eth.contract(
      address = deployed_address,
      abi = self.abi
    )
    return deployed

  def get_concise_instance(self, deployed_address):
    return ConciseContract(self.from_deployed_instance(deployed_address))

  def update_function(self, deployed_instance, function, *params):
    txhash = deployed_instance.functions[function](*params).transact()
    self.w3.eth.waitForTransactionReceipt(txhash)
    print('Function updated: {} {}'.format(function, *params))


