Bitcoin is a fortress of numbers that is entirely mathematical. It will be challenging, unsafe, prone to user mistake, and frustrating if you have to read, copy, or write in 256 sequences of 1s and 0s as private keys to claim ownership of a specific quantity of bitcoin. A standard system that considers security, known as BIP39, has been designed to make it simpler and safer for all users. BIP39 may readily provide you a sequence of words known as your mnemonic seed. By putting the words in the right order, you may deduce the private key of a bitcoin account from the mnemonic seed. Therefore, money kept in a bitcoin account can be stolen if the mnemonic seed is known.

It is nearly hard to brute force a 12 word mnemonic and find a private key holding bitcoin. As we know, the number of conceivable combinations is incalculably huge.

However, when more words are learned, the entropy decreases.

`main.py` will:

1.  Go through all of the BIP standard's available 12th word combinations.
2.  Using the 12 word mnemonic, generate the corresponding private key.
3.  Establish a connection to a distant complete node target.
4.  Check the whole node chain history to determine whether there are any money in the wallet.
5.  Report the right 12th word used to access the wallet so that we may inform the owner of their error (or steal the funds for yourself).
