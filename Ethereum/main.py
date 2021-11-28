# pip install pycoin
# pip install pysha3

import sha3
import datetime
from pycoin.ecdsa.secp256k1 import secp256k1_generator
import hashlib, secrets

def checksum_encode(addr_str): 
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

def sha3_256Hash(msg):
    hash_bytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hash_bytes, byteorder="big")

def sign_ecdsa_secp256k1(msg, private_key):
    return secp256k1_generator.sign(private_key, sha3_256Hash(msg))

def verify_ecdsa_secp256k1(msg, sig, public_key):
    return secp256k1_generator.verify(public_key, sha3_256Hash(msg), sig)
    
class Block:
    def __init__(self, previous_hash, data, private_key, public_key):
        self.previous_hash = previous_hash
        self.data = data
        self.signature = sign_ecdsa_secp256k1(str(data), private_key)
        self.public_key = public_key
        self.timestamp = datetime.datetime.now()
        self.proof_of_work = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        k = sha3.keccak_256()
        data = (str(self.previous_hash) + 
            str(self.data) +
            str(self.timestamp) +
            str(self.proof_of_work))
        k.update(data.encode('utf-8'))
        return k.hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.proof_of_work += 1
            self.hash = self.calculate_hash()
    

class Blockchain:
    def __init__(self):
        genesis_block = Block("0", {'isGenesis': True}, 0, 0)
        self.chain = [genesis_block]
        self.difficulty = 1

    def add_block(self, data, private_key, public_key):
        last_block = self.chain[len(self.chain) - 1]
        new_block = Block(last_block.hash, data, private_key, public_key)
        new_block.mine(self.difficulty) # find a hash for new block
        self.chain.append(new_block)

    def is_valid(self):
        for i in range (1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# print(blockchain.chain[0].data)
# print(blockchain.chain[0].previous_hash)
# print(blockchain.chain[0].hash)
# print(blockchain.chain[0].proof_of_work)
# print(blockchain.chain[1].data)
# print(blockchain.chain[1].previous_hash)
# print(blockchain.chain[1].hash)
# print(blockchain.chain[1].proof_of_work)
# print(blockchain.chain[1].public_key)
# print(blockchain.chain[1].signature)
# print("Signature is", verify_ecdsa_secp256k1(str(blockchain.chain[1].data), blockchain.chain[1].signature, blockchain.chain[1].public_key))
# print("Blockchain state is", blockchain.is_valid())
# blockchain.chain[1].data = {
#     'from': 'Alice',
#     'to': 'Bob',
#     'amount': 1000,
# }
# print("Signature is", verify_ecdsa_secp256k1(str(blockchain.chain[1].data), blockchain.chain[1].signature, blockchain.chain[1].public_key))
# print("Blockchain state is", blockchain.is_valid())
# print(blockchain.chain[2].data)
# print(blockchain.chain[2].previous_hash)
# print(blockchain.chain[2].hash)
# print(blockchain.chain[2].proof_of_work)
# print('done')

print("Welcome to Cryplet Alice! Here's a simple demo of a blockchain!\n")
print("Enter 0 to exit")
print("Enter 1 to generate private key")
print("Enter 2 to get your public key")
print("Enter 3 to get your Ethereum address")
print("Enter 4 to send ether")
print("Enter 5 to verify a block")
print("Enter 6 to verify the whole blockchain")
print("Enter 7 to  change the ether sent to Bob at block 1 to 1000")
print("Enter 8 to view the block")
print("Enter 9 to view the number of hashes needed for current difficulty")
print("Enter 10 to change difficulty of mining")
command = -1
blockchain = Blockchain()
while command != 0:
    command = int(input("Enter your command: "))
    if command == 0:
        break
    elif command == 1:
        alice_private_key = secrets.randbelow(secp256k1_generator.order())
        print("Your private key is:", hex(alice_private_key), "\n")
    elif command == 2:
        alice_public_key = (secp256k1_generator * alice_private_key)
        print("Your public key is: (" + hex(alice_public_key[0]) + ", " + hex(alice_public_key[1]) + ")", "\n")
    elif command == 3:
        keccak = sha3.keccak_256()
        keccak.update(str(alice_public_key).encode('utf-8'))
        alice_address = keccak.hexdigest()[24:]
        print("Your ethereum address is: ", checksum_encode(alice_address), "\n")
    elif command == 4:
        recipient = input("Enter the name of recipient: ")
        amount = int(input("Enter the amount to send: "))
        blockchain.add_block({
            'from': 'Alice',
            'to': recipient,
            'amount': amount,
        }, alice_private_key, alice_public_key)
        blockchain_length = len(blockchain.chain)
        print("Here are your new block details:")
        blockchain_length = len(blockchain.chain)
        print("Data: ", blockchain.chain[blockchain_length-1].data)
        print("Previous block hash: ", blockchain.chain[blockchain_length-1].previous_hash)
        print("Block hash: ", blockchain.chain[blockchain_length-1].hash)
        print("Proof of Work/Nonce: ", blockchain.chain[blockchain_length-1].proof_of_work)
        print("Signature of transaction: ", blockchain.chain[blockchain_length-1].signature, "\n")
    elif command == 5:
        block_num = int(input("Enter the block number to verify: "))
        is_valid = verify_ecdsa_secp256k1(str(blockchain.chain[block_num].data), blockchain.chain[block_num].signature, blockchain.chain[block_num].public_key)
        if is_valid:
            print("Valid block! Signature matches public key of sender and message.\n")
        else:
            print("Invalid block! Signature does not match the public key of sender and message.\n")
    elif command == 6:
        is_valid = blockchain.is_valid()
        if is_valid:
            print("Blockchain state is valid!\n")
        else:
            print("Blockchain state is invalid!\n")
    elif command == 7:
        blockchain.chain[1].data = {
            'from': 'Alice',
            'to': 'Bob',
            'amount': 1000,
        }
        print("New data: ", blockchain.chain[1].data, "\n")
    elif command == 8:
        block_num = int(input("Enter the block number: "))
        print("Data: ", blockchain.chain[block_num].data)
        print("Previous block hash: ", blockchain.chain[block_num].previous_hash)
        print("Block hash: ", blockchain.chain[block_num].hash)
        print("Proof of Work/Nonce: ", blockchain.chain[block_num].proof_of_work)
        print("Signature of transaction: ", blockchain.chain[block_num].signature, "\n")
    elif command == 9:
        hashes_tried = 0
        blockchain_length = len(blockchain.chain)
        print("Curent difficulty is:", blockchain.difficulty)
        print("Adding 30 blocks to get a sample...")
        for i in range(30):
            blockchain.add_block({
            'from': 'Alice',
            'to': recipient,
            'amount': amount,
            }, alice_private_key, alice_public_key)
            hashes_tried += blockchain.chain[blockchain_length-1].proof_of_work
            blockchain_length += 1
            if i % 3 == 0:
                print("Block", i, "Number of hashes tried: ", blockchain.chain[blockchain_length-1].proof_of_work)
        print("Average number of hashes tried is", "{:.2f}".format(hashes_tried / 30))
    elif command == 10:
        new_difficulty = int(input("Enter new difficulty: "))
        blockchain.difficulty = new_difficulty
