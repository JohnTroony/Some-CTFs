import time
import base64
import hashlib

# AfricaHackon 2018 CTF Qulaifiers
# This script is part of an inscure API function used by an online banking application 
# 	to transport card data from a user session to the backend for payment processing.
############################################################################################

# Crack the CARD Data and SESSIONKEY used to generate the following intercepted data :
# CIPHER TEXT : HRUfBElPJwAaC398XVdWCgJMLxRRBAIeWURODREeUgwUDVBbXVVxe3N8e1NWXEhOB1VYH2ohKz4lNiRra3x3fHt8FxknIiVtbnNxdmBu
# CARD UID : 52f97376e3f263579e8b2e295ba9fcf4
########################  

seed = time.strftime('%M%S')
standard = "mklam0fwj0cncds0if0wnoaDNCLKadnqw0mk8JDSNLDAVLLNSJD09DASPIJADSIOIN"
variable = "Strathmore_"+seed
SESSIONKEY = variable + standard

def xorme(data, key):
    xorry = bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))
    encoded_xorry = base64.b64encode(xorry)
    return encoded_xorry

def cc_uid(message):
	md5hash = hashlib.md5(message.encode())
	uid = md5hash.hexdigest()
	return uid


CARD = "some credit card data information goes here"
CIPHERTEXT = xorme(CARD, SESSIONKEY)
UID = cc_uid(CARD)

print "CREDIT CARD : " + CARD
print "SESSION KEY : " + SESSIONKEY
print "CIPHER TEXT : " + CIPHERTEXT
print "CARD UID : " + UID
