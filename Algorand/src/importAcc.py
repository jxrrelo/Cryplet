import params
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

wallethandle = client.init_wallet_handle(walletid, "pass123")
print("Wallet Handle:", wallethandle)

kpriv1, addr1 = "3pNOCIRkltSblIcacJVZBUWytnkRLi+iKcOnMA5vBx/QFDgNDYm6UMwMHRdNg6dvxBnKE9sNTj5NKF22NVYnfw==", "2AKDQDINRG5FBTAMDULU3A5HN7CBTSQT3MGU4PSNFBO3MNKWE574DWDK74"
kpriv2, addr2 = "vLVOkRrD51YAACeCG5w955kc1F2Vro5ROUHVgM/PBaIQYH9kBDrZsI9C4skKguOjpQC6X6NSmS8wpNsJcH0VLg==", "CBQH6ZAEHLM3BD2C4LEQVAXDUOSQBOS7UNJJSLZQUTNQS4D5CUXJSOYX6E"
print("Private Key 1:", kpriv1)
print("Address 1:", addr1)

print("Private Key 2:", kpriv2)
print("Address 2:", addr2)

mn1 = mnemonic.from_private_key(kpriv1)
print("Mnemonic 1:", mn1)

mn2 = mnemonic.from_private_key(kpriv2)
print("Mnemonic 2:", mn2) 

importedaccount1 = client.import_key(wallethandle, kpriv1)
importedaccount2 = client.import_key(wallethandle, kpriv2)

print("Imported Account 1: ", importedaccount1)
print("Imported Account 2: ", importedaccount2)