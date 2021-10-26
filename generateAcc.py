#Generate standalone account with account info to be imported into wallet

from algosdk import mnemonic, encoding, account

pk, addr = account.generate_account()
mn = mnemonic.from_private_key(pk)

print("Private Key: ", pk)
print("Mnemonic Phrase: ", mn)
print("Address: ", addr)

if encoding.is_valid_address(addr):
    print("The address is valid!")
else:
    print("The address is invalid!")
