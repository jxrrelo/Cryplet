import params
from algosdk import kmd, mnemonic
from algosdk.wallet import Wallet

client = kmd.KMDClient(params.kmd_token, params.kmd_address)

wallet = Wallet("myWallet", "pass123", client)

wallet.info()

masterkey = wallet.export_master_derivation_key()
print("Master Derivation Key:", masterkey)

backup = mnemonic.from_master_derivation_key(masterkey)
print("Wallet Backup Phrase:", backup)

print("Wallet ID:", wallet.id)
print("Accounts:", wallet.list_keys())