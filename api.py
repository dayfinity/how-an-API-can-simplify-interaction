import json
from pathlib import Path

from web3 import Web3
from eth_account import Account

RPC_NODE = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

client = Web3(
    Web3.HTTPProvider(RPC_NODE)
)

wallet = Account.from_key(KEY)

record = {}

record["API"] = "API"
record["architecture"] = "architecture"
record["endpoints"] = "endpoints"

transaction = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 120000,
    "gasPrice": client.to_wei(
        5,
        "gwei"
    ),
    "nonce": client.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    transaction
)

record["signature"] = len(
    s
