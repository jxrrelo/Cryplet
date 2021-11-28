# pip install ecdsa
# pip install pysha3

from ecdsa import SigningKey, SECP256k1
import sha3

def checksum_encode(addr_str): # Takes a hex (string) address as input
    keccak = sha3.keccak_256()
    out = ''
    addr = addr_str.lower().replace('0x', '')
    keccak.update(addr.encode('ascii'))
    hash_addr = keccak.hexdigest()
    for i, c in enumerate(addr):
        if int(hash_addr[i], 16) >= 8:
            out += c.upper()
        else:
            out += c
    return '0x' + out

keccak = sha3.keccak_256()

priv = SigningKey.generate(curve=SECP256k1)
pub = priv.get_verifying_key().to_string()

keccak.update(pub)
address = keccak.hexdigest()[24:]

def test(addrstr):
    assert(addrstr == checksum_encode(addrstr))

test('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed')
test('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359')
test('0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB')
test('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb')
test('0x7aA3a964CC5B0a76550F549FC30923e5c14EDA84')

print("Private key:", priv.to_string().hex())
print("Public key: ", pub.hex())
print("Address:    ", checksum_encode(address))






# # pip install tinyec
# # pip install pycryptodome

# from tinyec import registry
# from Crypto.Cipher import AES
# import hashlib, secrets, binascii
# from ecdsa import SigningKey, SECP256k1

# def encrypt_AES_GCM(msg, secretKey):
#     aesCipher = AES.new(secretKey, AES.MODE_GCM)
#     ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
#     return (ciphertext, aesCipher.nonce, authTag)

# def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
#     aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
#     plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
#     return plaintext


# def ecc_point_to_256_bit_key(point):
#     sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
#     sha.update(int.to_bytes(point.y, 32, 'big'))
#     return sha.digest()

# # curve = registry.get_curve('secp256k1')
# curve = SECP256k1

# def encrypt_ECC(msg, pubKey):
#     ciphertextPrivKey = secrets.randbelow(curve.field.n)
#     sharedECCKey = ciphertextPrivKey * pubKey
#     secretKey = ecc_point_to_256_bit_key(sharedECCKey)
#     ciphertext, nonce, authTag = encrypt_AES_GCM(msg, secretKey)
#     ciphertextPubKey = ciphertextPrivKey * curve.g
#     return (ciphertext, nonce, authTag, ciphertextPubKey)

# def decrypt_ECC(encryptedMsg, privKey):
#     (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
#     sharedECCKey = privKey * ciphertextPubKey
#     secretKey = ecc_point_to_256_bit_key(sharedECCKey)
#     plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
#     return plaintext

# msg = b'Text to be encrypted by ECC public key and ' \
#       b'decrypted by its corresponding ECC private key'
# print("original msg:", msg)
# privKey = secrets.randbelow(curve.field.n)
# pubKey = privKey * curve.g

# encryptedMsg = encrypt_ECC(msg, pubKey)
# encryptedMsgObj = {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'nonce': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2]),
#     'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
# }
# print("encrypted msg:", encryptedMsgObj)

# decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
# print("decrypted msg:", decryptedMsg)