"""
    Make a transcation; send/receive from one account to another
"""

import params
from algosdk import kmd
from algosdk import transaction, account

client = kmd.KMDClient(params.kmd_token, params.kmd_address)

sender = "6BFUSRWJPMW2UMRSSREE4GRSYLO55GHB3HQIKPCN57BUD5ABMCQT443X5Y" #4000252000000000 - default wallet
receiver = "RIIPVCPPMMJIWTUHXZVW3E6XOJI4QXG5F37AGIWVQU6I7RBLCPLAQL4PPU" #0 - myWallet
gen = "sandnet-v1"
gh = "8dH5NoDVzb7aBzFqry5PwYemvgMUNHNoQLkpjkV/SHI="

txn = transaction.PaymentTxn(sender, 5, 1, 100, gh, receiver, 200)

# sign transaction1
stxn = txn.sign(pk_account_a)

# send them over network
sent = client.send_transaction(stxn)

# print txid
print(sent) 