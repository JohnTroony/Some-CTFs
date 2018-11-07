#!/bin/bash


#create our key pairs
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

#sign and verify
openssl dgst -sha1 -sign private.pem -out "$0".sha1 $0
openssl dgst -sha1 -verify public.pem -signature "$0".sha1 $0
