import params
import credentials
from algosdk import kmd, account, encoding, mnemonic

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

kpriv, addr = "eavzLKX0jSULDiTUiOfVAyu8EKJFFD5aAixrA1gwuzwdqtPOmxlVMVT3W6Cf78WxssKBenFrSrhHhCKjm8CYKQ==", "DWVNHTU3DFKTCVHXLOQJ736FWGZMFAL2OFVUVOCHQQRKHG6ATAU6TO2P3I"#account.generate_account()
print("Private Key:", kpriv)
print("Address:", addr)

mn = mnemonic.from_private_key(kpriv)
print("Mnemonic:", mn)