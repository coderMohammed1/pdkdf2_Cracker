import hashlib
import os
import base64
import binascii

passwords = []
iterations = 600000

# pbkdf2:sha256:iterations$salt:hash
salt =  "AMtzteQIG7yAbZIa"

with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as wlist:
    passwords = [line.strip() for line in wlist]

for password in passwords:    
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        iterations,
        dklen=32
    )

    hex_hash = binascii.hexlify(dk).decode()

    final = f"pbkdf2:sha256:{iterations}${salt}${hex_hash}"
    if final == 'pbkdf2:sha256:600000$AMtzteQIG7yAbZIa$0673ad90a0b4afb19d662336f0fce3a9edd0b7b19193717be28ce4d66c887133':
        print(password)
        break
