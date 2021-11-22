"""
    Generate kmd wallet that contains multiple accounts
"""

import params
from algosdk import kmd
from algosdk.wallet import Wallet

# create a kmd client
client = kmd.KMDClient(params.kmd_token, params.kmd_address)

# create a wallet object
wallet = Wallet("myWallet", "pass123", client)

# get wallet information
info = wallet.info()
print("Wallet name:", wallet.handle)

# create an account
address = wallet.generate_key()
print("New account:", address)

# delete the account
"""
try:
    delete = wallet.delete_key(address)
    print("Account deleted:", delete)
except:
    print("Invalid Account Address!")
"""