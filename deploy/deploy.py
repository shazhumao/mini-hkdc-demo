from solcx import compile_standard, install_solc
from web3 import Web3
import json, os
from dotenv import load_dotenv

load_dotenv()

install_solc("0.8.20")
with open("contracts/MiniHKDC.sol", "r") as file:
    source = file.read()

compiled = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "MiniHKDC.sol": {"content": source}
        },
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        }
    },
    solc_version="0.8.20",
    base_path="contracts",
    allow_paths=".,contracts,node_modules,contracts/node_modules"
)

with open("contracts/MiniHKDC.abi.json", "w") as f:
    json.dump(compiled['contracts']['MiniHKDC.sol']['MiniHKDC']['abi'], f)

bytecode = compiled['contracts']['MiniHKDC.sol']['MiniHKDC']['evm']['bytecode']['object']
abi = compiled['contracts']['MiniHKDC.sol']['MiniHKDC']['abi']

web3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
private_key = os.getenv("PRIVATE_KEY")
public_address = os.getenv("PUBLIC_ADDRESS")

MiniHKDC = web3.eth.contract(abi=abi, bytecode=bytecode)
nonce = web3.eth.get_transaction_count(public_address)

transaction = MiniHKDC.constructor().build_transaction({
    'chainId': int(os.getenv("CHAIN_ID")),
    'gas': 3000000,
    'gasPrice': web3.to_wei('10', 'gwei'),
    'nonce': nonce,
})
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
print("Deploy tx hash:", web3.to_hex(tx_hash))
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print("✅ Contract deployed at:", receipt.contractAddress)