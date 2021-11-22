import params
from algosdk import kmd, mnemonic
from algosdk.wallet import Wallet
import credentials

client = kmd.KMDClient(params.kmd_token, params.kmd_address)

walletid = None
wallets = client.list_wallets()
print("Wallet List:", wallets)

for wallet in wallets:
    if wallet.get("name") == "myWallet":
        walletid = wallet.get("id")
        break
    
print("Wallet ID:", walletid)

wallethandle = client.init_wallet_handle(walletid, credentials.walletpw)
print("Wallet Handle:", wallethandle)

accounts = client.list_keys(wallethandle)
print("Accounts:", accounts)
accountkey = client.export_key(wallethandle, credentials.walletpw, credentials.addr)
print("Account Key:", accountkey)
mn = mnemonic.from_private_key(accountkey)
print("Mnemonic:", mn)