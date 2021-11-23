# Cryplet

## Description
Cryplet, or a cryptocurrency wallet, is a physical medium which stores the private/public key pairs that allows cryptocurrency transactions to take place. In addition to this basic function of storing the keys, a cryptocurrency wallet more often also offers the functionality of encrypting and/or signing information.

## Motivations
Just like the way people keep cash or cards in a physical wallet, bitcoins are also stored in a wallet—a digital wallet. The digital wallet can be hardware-based or web-based. The wallet can also reside on a mobile device, on a computer desktop, or kept safe by printing the private keys and addresses used for access on paper. But how safe are any of these digital wallets? The answer to this depends on how the user manages the wallet. Every wallet contains a set of private keys without which the bitcoin owner cannot access the currency. The biggest danger in bitcoin security is the individual user perhaps losing the private key or having the private key stolen. Without the private key, the user will never have access to his/her bitcoins again. Besides this problem, a user can also lose his/her bitcoin by computer malfunctions (crashing a hard drive), hacking, or simply losing the physical device where the digital wallet resides. While there are many factors that contribute to security such as smart contract bugs, this project focuses exclusively on the cryptography uses and its application. We start with how private keys are generated, then how public keys and addresses are subsequently derived. Then we examine its security and research that looks into its weaknesses.

This project focuses on 2 cryptocurrencies - Ethereum and Algorand. Both of these cryptocurrencies offer a wide range of resources that enables the expedition of the development phase, some of which include cryptographic library functions, online video explanations and research papers. Ethereum is undoubtedly one of the most popular platforms for building decentralised applications, with many high value use cases such as decentralised finance. Algorand, on the other hand, has several discussions and researches revolving around it, explaining why it is in pole position to take over the lead in the smart contract platform space. With the study of Ethereum and Algorand, this project aims to sieve and discuss possible similarities and differences in their security implementations.

## Research
### Ethereum

### Algorand
(to be elaborated)
- security primitives
- how passphrase is generated and linked to private key

## Development
### Ethereum

### Algorand
(to be elaborated)
- Use of docker
- sandboxing
- uses of scripts (generating wallet/account)

## Usage
### Ethereum

### Algorand
1. Ensure [Docker](https://docs.docker.com/get-docker/) is installed locally
2. Run Docker Daemon
3. Run `./sandbox up testnet` to spin up a Docker container defaulting to the testnet binaries.
4. Run `./sandbox down` to stop the Docker container
5. (More to be added)

## Resources
- [Ethereum](https://ethereum.org/en/)
- [Algorand](https://www.algorand.com/)
- [Etherscan](https://etherscan.io/)
- [Algosdk API](https://py-algorand-sdk.readthedocs.io/en/latest/)
- [Idea behind Mnemonic phrase and generating address](https://medium.com/mycrypto/the-journey-from-mnemonic-phrase-to-address-6c5e86e11e14)
- [How Bitcoin Wallets Work](https://www.youtube.com/watch?v=GSTiKjnBaes)
- [bip39 standard](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
- [Generating Secure Crypto Wallets and Accounts](https://www.youtube.com/watch?v=x-P-nmhiO-g)

