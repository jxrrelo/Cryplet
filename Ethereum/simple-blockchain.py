import sha3
import datetime

class Block:
    def __init__(self, previousHash, data):
        self.previousHash = previousHash
        self.data = data
        self.timeStamp = datetime.datetime.now()
        self.proofOfWork = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        k = sha3.keccak_256()
        data = (str(self.previousHash) + 
            str(self.data) +
            str(self.timeStamp) +
            str(self.proofOfWork))
        k.update(data.encode('utf-8'))
        return k.hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.proofOfWork += 1
            self.hash = self.calculateHash()
    

class Blockchain:
    def __init__(self):
        genesisBlock = Block("0", {'isGenesis': True})
        self.chain = [genesisBlock]

    def addBlock(self, data):
        lastBlock = self.chain[len(self.chain) - 1]
        newBlock = Block(lastBlock.hash, data)
        newBlock.mine(1) # find a hash for new block
        self.chain.append(newBlock)

    def isValid(self):
        for i in range (1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True

blockchain = Blockchain()
blockchain.addBlock({
    'from': 'Alice',
    'to': 'Bob',
    'amount': 100,
})
blockchain.addBlock({
    'from': 'Bob',
    'to': 'Eve',
    'amount': 10,
})

print(blockchain.chain[0].data)
print(blockchain.chain[0].previousHash)
print(blockchain.chain[0].hash)
print(blockchain.chain[0].proofOfWork)
print(blockchain.chain[1].data)
print(blockchain.chain[1].previousHash)
print(blockchain.chain[1].hash)
print(blockchain.chain[1].proofOfWork)
print(blockchain.chain[2].data)
print(blockchain.chain[2].previousHash)
print(blockchain.chain[2].hash)
print(blockchain.chain[2].proofOfWork)
print('done')