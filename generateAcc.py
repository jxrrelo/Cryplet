"""
    Generate standalone account with account info to be imported into wallet
"""
import params
from algosdk import mnemonic, encoding, account
from algosdk.v2client import algod

algod_client = algod.AlgodClient(params.algod_token, params.algod_address)

account_info = algod_client.account_info("2AKDQDINRG5FBTAMDULU3A5HN7CBTSQT3MGU4PSNFBO3MNKWE574DWDK54")
print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

pk, addr = account.generate_account()
mn = mnemonic.from_private_key(pk)

print("Private Key: ", pk)
print("Mnemonic Phrase: ", mn)
print("Address: ", addr)

if encoding.is_valid_address(addr):
    print("The address is valid!")
else:
    print("The address is invalid!")

