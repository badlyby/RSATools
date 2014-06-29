When using need to install python M2Crypto library
Ubuntu Linux:
sudo apt-get install python-m2crypto

Generate keys:
python genkey.py
Need enter the passphrase, else private key won't be able to store

Or:
./genrsakey.sh

Encryption: need to generate the pub-key.pem
python encrypto.py file

Decryption: need to generate the key.pem
python decrypto.py file



使用时需要安装python M2Crypto库
Ubuntu Linux:
sudo apt-get install python-m2crypto

生成密钥:
python genkey.py
需要设置密码，否则私钥无法储存
或:
./genrsakey.sh

加密:	需要生成的pub-key.pem
python encrypto.py 文件

解密:	需要生成的key.pem
python decrypto.py 文件
