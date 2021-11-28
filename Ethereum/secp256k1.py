# pip install pycoin

from pycoin.ecdsa.secp256k1 import secp256k1_generator
import hashlib, secrets

def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")

def sign_ecdsa_secp256k1(msg, priv_key):
    return secp256k1_generator.sign(priv_key, sha3_256Hash(msg))

def verify_ecdsa_secp256k1(msg, sig, pub_key):
    return secp256k1_generator.verify(pub_key, sha3_256Hash(msg), sig)

# ECDSA sign message (using the curve secp256k1 + SHA3-256)
msg = "Message for ECDSA signing"
privKey = secrets.randbelow(secp256k1_generator.order())
signature = sign_ecdsa_secp256k1(msg, privKey)
print("Message:", msg)
print("Private key:", hex(privKey))
print("Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))

# ECDSA verify signature (using the curve secp256k1 + SHA3-256)
pubKey = (secp256k1_generator * privKey)
valid = verify_ecdsa_secp256k1(msg, signature, pubKey)
print("\nMessage:", msg)
print("Public key: (" + hex(pubKey[0]) + ", " + hex(pubKey[1]) + ")")
print("Signature valid?", valid)

# ECDSA verify tampered signature (using the curve secp256k1 + SHA3-256)
msg = "Tampered message"
valid = verify_ecdsa_secp256k1(msg, signature, pubKey)
print("\nMessage:", msg)
print("Signature (tampered msg) valid?", valid)