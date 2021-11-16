"""
    Make a transcation; send/receive from one account to another
"""

import params
import credentials
from algosdk import kmd
from algosdk import transaction, account
from algosdk.v2client import algod
from algosdk.future.transaction import PaymentTxn

client = kmd.KMDClient(params.kmd_token, params.kmd_address)
acl = algod.AlgodClient(params.algod_token, params.algod_address)


account_info = acl.account_info("2AKDQDINRG5FBTAMDULU3A5HN7CBTSQT3MGU4PSNFBO3MNKWE574DWDK74")
print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

param = acl.suggested_params()
param.fee = 1000
param.flat_fee = True
note = "Hello World".encode()

sender = "2AKDQDINRG5FBTAMDULU3A5HN7CBTSQT3MGU4PSNFBO3MNKWE574DWDK74" #4000252000000000 - default wallet
receiver = "CBQH6ZAEHLM3BD2C4LEQVAXDUOSQBOS7UNJJSLZQUTNQS4D5CUXJSOYX6E" #0 - myWallet
gen = "testnet-v1.0"
gh = "SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI="

txn = PaymentTxn(sender, param, receiver, 100000, None, note)

# sign transaction1
stxn = txn.sign(credentials.kpriv)

# send them over network
txid = acl.send_transaction(stxn)

# print txid
print("Successfully sent transaction with txID: {}".format(txid)) 
