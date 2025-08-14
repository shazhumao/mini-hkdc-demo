import json
from backend.config import web3, PRIVATE_KEY, PUBLIC_ADDRESS, CONTRACT_ADDRESS

with open("contracts/MiniHKDC.abi.json") as f:
    abi = json.load(f)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

def mint(to, amount):
    nonce = web3.eth.get_transaction_count(PUBLIC_ADDRESS)
    txn = contract.functions.mint(to, int(amount)).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 200000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return web3.to_hex(tx_hash)

def burn(from_addr, amount):
    nonce = web3.eth.get_transaction_count(PUBLIC_ADDRESS)
    txn = contract.functions.burn(from_addr, int(amount)).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 200000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)

def get_balance(address):
    return contract.functions.balanceOf(address).call()
