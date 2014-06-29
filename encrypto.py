#!/usr/bin/python

import M2Crypto as m2c
import sys

RSAbits = 2048
block_size = RSAbits / 16

def encrypt_block(pubkey, data):
	encrypted = pubkey.public_encrypt(data, m2c.RSA.pkcs1_padding)
	return encrypted

def encrypt_data(pubkey, data):
	encrypted = ""
	lng = len(data)
	offs = 0
	while lng > block_size:
		encrypted = encrypted + encrypt_block(pubkey, data[offs:offs+block_size])
		offs = offs + block_size
		lng = lng - block_size
	if lng > 0:
		encrypted = encrypted + encrypt_block(pubkey, data[offs:offs+lng])
	return encrypted

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc == 3:
		outname = sys.argv[2]
	else:
		outname = sys.argv[1]+".rsa"
	pubkey = m2c.RSA.load_pub_key('pub-key.pem')
	data = file(sys.argv[1], 'rb').read()
	encrypted = encrypt_data(pubkey, data)
	file(outname, 'wb').write(encrypted)

