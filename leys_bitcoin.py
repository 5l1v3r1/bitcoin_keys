#!/usr/bin/env python

import bitcoin

def function_keys():

 valid_private_key = False                #randomize private key

 while not valid_private_key:
  private_key = bitcoin.random_key()
  decode_private_key = bitcoin.decode_privkey(private_key, 'hex')
  valid_private_key = 0 < decode_private_key < bitcoin.N

 print "Private Key (hex) is:", private_key
 print "Private Key (decimal) is:", decode_private_key
 wif_encode_private_key = bitcoin.encode_privkey(decode_private_key, 'wif')
 print "Private key (WIF) is:", wif_encode_private_key     # convert private key to wif format

 compressed_private_key = private_key + '01'
 print "Private key Compressed (hex) is:", compressed_private_key  # add '01' to indicate compressed private key

 wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
 print "Private Key (Wif-compressed) is:", wif_compressed_private_key

 public_key = bitcoin.fast_multiply(bitcoin.G, decode_private_key)  # multiply EC generator with the private key to have public key point
 print "Public Key (x, y) coordinates is:", public_key

 hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')   # encoded public key with '04'
 print "Public Key (hex) is:", hex_encoded_public_key

 (public_key_x, public_key_y) = public_key               # compressed public key
 if (public_key_y %2) == 0:
  compressed_prefix = '02'
 else:
  compressed_prefix = '03'
  hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
 print "Compressed Public Key (hex) is:", hex_compressed_public_key
 print "Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(public_key)

 print "Compressed Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(hex_compressed_public_key)
 
function_keys()
