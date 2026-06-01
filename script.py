import hashlib
from web3 import Web3
import json
import socket

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

contract_address = '0x406b029eEA73524B2990c726080D5BE3fe55a708'
contract_abi = json.loads('[{"inputs":[{"internalType":"string","name":"_message","type":"string"},{"internalType":"string","name":"_hash","type":"string"}],"name":"addLog","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

contract = w3.eth.contract(address=contract_address, abi=contract_abi)
w3.eth.default_account = w3.eth.accounts[0]

log_message = f"Failed password from {socket.gethostbyname(socket.gethostname())} port 22 ssh2"
log_hash = hashlib.sha256(log_message.encode('utf-8')).hexdigest()

print(f"Log text: {log_message}")
print(f"SHA-256 Hash: {log_hash}")

try:
    tx_hash = contract.functions.addLog(log_message, log_hash).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Log usuccessfulz written. ID: {tx_hash.hex()}")
except Exception as e:
    print(f"Network error: {e}")