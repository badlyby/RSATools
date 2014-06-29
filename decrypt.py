#!/usr/bin/python

import M2Crypto as m2c
import sys

RSAbits = 2048
block_size = RSAbits / 8

def decrypt_block(key, data):
	decrypted = key.private_decrypt(data, m2c.RSA.pkcs1_padding)
	return decrypted

def decrypt_data(key, data):
	decrypted = ""
	lng = len(data)
	offs = 0
	while lng > block_size:
		decrypted = decrypted + decrypt_block(key, data[offs:offs+block_size])
		offs = offs + block_size
		lng = lng - block_size
	if lng > 0:
		decrypted = decrypted + decrypt_block(key, data[offs:offs+lng])
	return decrypted

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc == 3:
		outname = sys.argv[2]
	else:
		nlen = len(sys.argv[1])
		if (nlen > 4) and (sys.argv[1][nlen-4:nlen] == ".rsa"):
			outname = sys.argv[1][0:nlen-4]
		else:
			outname = sys.argv[1]+".dersa"
	key = m2c.RSA.load_key('key.pem')
	data = file(sys.argv[1], 'rb').read()
	decrypted = decrypt_data(key, data)
	file(outname, 'wb').write(decrypted)

