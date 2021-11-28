# Cryplet

## Description
Cryptocurrencies have been taking off lately so it will be interesting to see how a simple transaction could be constructed and verified cryptographically. Cryplet, or a cryptocurrency wallet, is a physical or software medium which stores the private/public key pairs that allows cryptocurrency transactions to take place. In addition to this basic function of storing the keys, a cryptocurrency wallet more often also offers the functionality of encrypting and/or signing information. 

## Motivations
Just like the way people keep cash or cards in a physical wallet, bitcoins and other cryptocurrencies can be thought of as being stored in a wallet that can be hardware-based or web-based. The wallet can also reside on a mobile device, on a computer desktop, or kept safe by printing the private keys and addresses used for access on paper. But how safe are any of these digital wallets? The answer to this depends on how the user manages the wallet. Every wallet contains a set of private keys without which the owner cannot access their cryptocurrency. The biggest danger in cryptocurrency security is perhaps the individual user revealing the private key or developers who did not securely implement their applications as we shall see some examples later. Without the private key, the user will never have access to his/her cryptocurrencies again. Besides this problem, a user can also lose his/her cryptocurrencies by computer malfunctions (crashing a hard drive), hacking, or simply losing the physical device where the digital wallet resides. While there are many factors that contribute to security such as smart contract bugs, this project focuses exclusively on the cryptography and its application. We start with how private keys are generated, then how public keys and addresses are subsequently derived. Then we construct a simple transaction and verify it. Finally, we examine its security and research that looks into its weaknesses.

This project focuses on 2 cryptocurrencies - Ethereum and Algorand. Both of these cryptocurrencies offer a wide range of resources that enables the expedition of the development phase, some of which include cryptographic library functions, online video explanations and research papers. Ethereum is undoubtedly one of the most popular platforms for building decentralised applications, with many high value use cases such as decentralised finance. Algorand, on the other hand, has several discussions and researches revolving around it, explaining why it is in pole position to take over the lead in the smart contract platform space. With the study of Ethereum and Algorand, this project aims to cover sufficient breadth and depth, sieving out and discussing possible similarities and differences in their security implementations.

## Research
To make private keys user friendly, both blockchains support the use of a Mnemonic phrase which performs the same function as private keys. Mnemonic phrases are a human-readable version of the private keys. The user can sign transactions and recover lost accounts using part of their mnemonic phrase. Mnemonic or seed phrases can range from 12 - 25 words depending on the blockchain ecosystem. However, there are some notable differences that will be discussed.

### Ethereum
#### Private key, public key, address generation
Private keys are generated as random 256 bits, which is 64 (hex) characters or 32 bytes. After this, Ethereum public keys (128 characters / 64 bytes) are created using an algorithm called Elliptic Curve Digital Signature Algorithm (ECDSA). Ethereum uses secp256k1 to generate public keys. Public key is a point in this Elliptic curve algorithm. Although the public key has twice the number of bits as the private key, the actual number of public keys are only as many as the number of private keys to start with. In order to create an Ethereum Addresses, keccak256 hash algorithm is applied to the public keys and the first 24 hex characters are dropped. We demo this in the presentation.

#### Verifying transactions with digital signatures
ECC is also used to sign transactions with the private key to produce signature. This signature can be used to verify if a particular message has been signed by a particular person's private key. The verification function takes in the signature, the message and the public key which we will demo in the presentation.

#### Hash functions for proof of work
Hash functions are also used to determine the proof of work difficulty. The meta data of the block is hashed but in order to generate a valid block hash, the number of zeroes in the hash must be at least equal to the difficulty level. In our demo, we used a difficulty level up to 3 but on the mainnnet the diffuclty level is actually 19. Due to the properties of the hash function, all outputs are equally likely so the chances of finding a valid hash is 1 / 16^difficulty. It is also almost impossible to find the pre-image even if we know the difficulty beforehand, which ensures progress freeness and fairness in mining. This is also demonstrated in the presentation.

#### Security Research
We also did more research on the security of Ethereum blockchain wallets. In short, the cryptography is strong but the shortcomings appear in developers' implementations as well as end users lack of knowledge on how to generate safe keys and keep them secure.

#### Parity Wallet with Empty Passphrase
Many wallets have a recovery phrase feature where your private keys can be derived from in case you switch wallets or just for ease of remembering. But what happens when one is too lazy to even have a recovery phrase and leave this field empty? Well, it turns out quite a number of people had this idea. An empty recovery phrase (“”) using the Parity wallet gives a private key 0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7. The address 0x00a329c0648769a73afac7f9381e08fb43dbea72 is then derived from it. There have been 8772 transactions on this address for a total of 5215 ETH by 2019. This address is very active and being monitored for inbound transactions which are immediately transferred out by one of many private key holders watching this address. Unlike hacks due to bad private key generation above which has decreased over time, the number of hacks related to empty passphrases have only increased, likely as more new users discover cryptocurrency but did not have the knowledge to protect their private keys. There are almost 31,000 transactions now on this compromised address (Etherscan, 2021).
Fortunately, other wallets like MetaMask are much better. They do not allow users to come up with their own passphrase or brain wallets so it prevents this issue entirely. The reasoning is that it is highly unlikely we can generate enough entropy on our own. Rather, these more secure wallets generate the passphrase for users and ask them to save it.

#### Insufficiently Random Private Key Generation
One of the most important aspects of security is generating a truly random private key. Since Ethereum uses 256 bit private keys, the probability of getting a private key that is already used should only be 1 in 2^256.
But in a study done by ISE, they managed to find 732 clashing addresses and their corresponding private key which had Ether transactions with about 2^35 keys scanned and 1024 CPU hours (Ethercombing: Finding Secrets in Popular Places, 2019). These addresses had a combined transaction volume of 49,060! ISE found that these private keys were not truly randomly generated as most of them only had 32 bits of entropy either for the 32 most significant bits or the 32 least significant bits, meaning the rest of the 224 bits were probably just hard coded as 0. This is what allowed the researchers to comb through billions of addresses in just 8 hours with parallel computing. Needless to say, the balance of these addresses were a grand total of 0. Bad actors are scarily efficient. 
The address at 0x957cd4ff9b3894fc78b5134a8dc72b032ffbc464 belonging to whom people dub the “Blockchain Bandit” had back in 2019 44,744 ETH, which at today’s price of $4250, amounts to almost $200M! Fortunately, people have gotten wiser since then and from 2019 to November 2021, the Blockchain Bandit only managed to pilfer another 11 ETH, a fraction of the previous years (Etherscan, 2021). The researchers knew the Blockchain Bandit was watching these weak addresses for any incoming transactions and wanted to test how quickly they would transfer the funds out. When the researchers sent over $1 to one of the compromised addresses, the funds were transferred to the Blockchain Bandit instantly. Pretty scary indeed if you don’t generate or keep your keys safely.
However, the researchers did acknowledge that most addresses were safer than this, and on the contrary this might show just how secure the Ethereum system is. It is permissionless and available 24/7 for hackers and yet, the majority of funds are safe.

### Algorand
Algorand uses Ed25519 (Edwards-curve Digital Signature Algorithm) high-speed, high-security elliptic-curve signatures. The keys are produced through standard, open-source cryptographic libraries packaged with each of the SDKs. The key generation algorithm takes a random value as input and outputs two 32-byte arrays, representing a public key and its associated private key. The public key is transformed into an Algorand address, by adding a 4-byte checksum to the end of the public key and then encoding it in base32. The result is what both the developer and end-user recognize as an Algorand address. The address is 58 characters long.

The Algorand blockchain supports mnemonic keys and is generated during the account sign up. It is a 25-word pattern that best represents the private key and performs the same functions as the private keys. They are easily readable and easy to memorise as well. On the Algorand blockchain chain, mnemonic keys are generated by converting the user's private key string to an 11-bit integer to the bip-0039 English word list where the integer value maps to the word in the bip-0039 English word list with position same as the integer value. To illustrate, if an integer value is 2, it will map to the 2nd word on the bip-0039 English word list. This process of transforming the private keys to 11-bit integer and mapping it to bip-0039 English word list will generate 24-word mnemic keys. The bip-0039 English word is made up of about 2048 random words in an array and can also be termed as seed phrase.

## Development
### Ethereum
A basic blockchain is implemented to demonstrate how some of the security implementations of general blockchain wallets are utilised. Contents include generation of private and public keys and Ethereum address, digital signatures and verification, hash function in setting the proof of work difficulty.

### Algorand
The Algorand Blockchain Explorer will be used to demonstrate a real-life scenario of a transaction taking place on the testnet. A testnet is an instance of a blockchain powered by the same or a newer version of the underlying software, to be used for testing and experimentation without risk to real funds or the main chain. With the use of Docker, we can spin up a container defaulting to the testnet binaries to perform tests. This environment which we carry out the tests is also known as a sandbox, isolated from the mainnet.

Some scripts are written for the purpose of generating a wallet, setting up an account, importing an account into a wallet, etc.

## Usage
### Ethereum
1. Ensure pycoin and pysha3 are installed. pip install pycoin or pip install pysha3
2. Open main.py and run the program
3. Recommended to follow the flow in the presentation. Important to generate keys first.

### Algorand
1. Ensure Python3 and [Docker](https://docs.docker.com/get-docker/) is installed locally
2. Run the Docker Daemon
3. Run `./sandbox up testnet` to spin up a Docker container defaulting to the testnet binaries (`./sandbox down` to stop the Docker container). This might take a while as the network updates itself using fast catch up.
4. Run `python3 generateWallet.py` to create a wallet
5. Run `python3 importAcct.py` to import 2 custom accounts that have already been pre-loaded with some testnet credits.

## Resources
- [Ethereum](https://ethereum.org/en/)
- [Algorand](https://www.algorand.com/)
- [Etherscan](https://etherscan.io/)
- [Algosdk API](https://py-algorand-sdk.readthedocs.io/en/latest/)
- [Idea behind Mnemonic phrase and generating address](https://medium.com/mycrypto/the-journey-from-mnemonic-phrase-to-address-6c5e86e11e14)
- [How Bitcoin Wallets Work](https://www.youtube.com/watch?v=GSTiKjnBaes)
- [bip39 standard](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
- [Generating Secure Crypto Wallets and Accounts](https://www.youtube.com/watch?v=x-P-nmhiO-g)
- [Security Dangers of NIST curves](http://www.hyperelliptic.org/tanja/vortraege/20130531.pdf)
- [Ethercombing: Finding Secrets In Popular Places](https://www.ise.io/casestudies/ethercombing/)
- [Etherscan: Blockchain Bandit's Wallet](https://etherscan.io/address/0x957cd4ff9b3894fc78b5134a8dc72b032ffbc464)
- [Etherscan: Parity Wallet Empty Passphrase](https://etherscan.io/address/0x00a329c0648769a73afac7f9381e08fb43dbea72)

