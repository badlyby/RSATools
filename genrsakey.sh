#!/bin/sh

openssl genrsa -out key.pem 2048
openssl rsa -in key.pem -pubout -out pub-key.pem
