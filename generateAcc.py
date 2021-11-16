"""
    Generate standalone account with account info to be imported into wallet
    
    Private Key:  3pNOCIRkltSblIcacJVZBUWytnkRLi+iKcOnMA5vBx/QFDgNDYm6UMwMHRdNg6dvxBnKE9sNTj5NKF22NVYnfw==
    Mnemonic Phrase:  knock demise aerobic embark coast vivid pill maple addict fiction proud expect goose horror mesh come echo pledge thunder apology broccoli swift wealth abandon castle
    Address:  2AKDQDINRG5FBTAMDULU3A5HN7CBTSQT3MGU4PSNFBO3MNKWE574DWDK74
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

