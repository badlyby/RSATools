#!/usr/bin/python

from M2Crypto import BIO, RSA

RSAbits = 2048

bio = BIO.MemoryBuffer()
rsa = RSA.gen_key(RSAbits, RSA.pkcs1_padding)
rsa.save_pem("key.pem", "aes_128_cbc")
rsa.save_pub_key("pub-key.pem")


