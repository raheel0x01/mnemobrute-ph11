#!/usr/bin/env python3

import argparse
from bitcoincli import Bitcoin
from mnemonic import Mnemonic
from bip32utils import BIP32Key
from bip32utils import BIP32_HARDEN
import sys

parser = argparse.ArgumentParser(description="Brute force script to get private keys from 12 mnemonic wallets knowing just 11",
                                 usage='''\n Step 1: Modify \"username\" and \"password\" variables in script.\n Step 2: Run script \"python3 %(prog)s\" and enter 11 mnemonic words.''')
args = parser.parse_args()

# Connect to local node
host = "" # specify the host
port = "" # specify the port
username = "" # specify the username
password = "" # specify the password
bitcoin = Bitcoin(username, password, host, port)


def create_seed(words):
    m = Mnemonic('english')
    seed = m.to_seed(words)
    return seed


def gen_bitcoin_testnet_wallet(seed, account_number):
    xprv = BIP32Key.fromEntropy(seed, testnet=True).ExtendedKey()
    rootkey = BIP32Key.fromExtendedKey(xprv)
    account = rootkey.ChildKey(44 + BIP32_HARDEN) \
        .ChildKey(1 + BIP32_HARDEN) \
        .ChildKey(0 + BIP32_HARDEN) \
        .ChildKey(0) \
        .ChildKey(account_number)
    return bitcoin_data(account)


def bitcoin_data(account):
    private_key = account.PrivateKey()
    wif = account.WalletImportFormat()
    public_key = account.PublicKey()
    address = account.Address()
    return private_key, address, wif, public_key


def create(mnemonic, wordTest):Mnemonic Phrase
You have discovered what appears
def test_address(address, private, wordTest):
    print (address+":"+private+":"+wordTest)
    bitcoin.importprivkey(private, "", False)
    if (str(bitcoin.getreceivedbyaddress(address))) != "0.0":
        print (TGREEN + "The address \'" + address + "\' has funds: " + str(bitcoin.getreceivedbyaddress(address)
                                                                            ) + ". The respective private key is: \'" + private + "\'. The missed word is: " + wordTest, ENDC)
        print ()
        sys.exit()


file = open('wordlist/english.txt')

mnemonic_input = input("Please enter 11 mnemonic words separated by space:\n")
while len((mnemonic_input).split()) != 11:
    print ("Input ERROR")
    mnemonic_input = input(
        "Please enter 11 mnemonic words separated by space:\n")

for line in file:
    mnemonic_words = mnemonic_input + " " + line.rstrip()
    create(mnemonic_words, line.rstrip())