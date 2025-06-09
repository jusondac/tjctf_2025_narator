#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random

def reproduce_exact_keys():
    """Reproduce the exact key generation as in enc.py"""
    # Simulate the exact execution of enc.py
    
    # First gen() call
    myrandom = random.Random(42)
    k1 = myrandom.randbytes(8)
    choices = list(myrandom.randbytes(6))
    k2 = b''
    for _ in range(8):
        k2 += bytes([choices[random.randint(0, 3)]])
    
    # Second gen() call - starts fresh with the same seed
    myrandom = random.Random(42)
    k3 = myrandom.randbytes(8)
    choices2 = list(myrandom.randbytes(6))
    k4 = b''
    for _ in range(8):
        k4 += bytes([choices2[random.randint(0, 3)]])
    
    return k1, k2, k3, k4

def decrypt_double_aes(ciphertext, k1, k2, k3, k4):
    """Decrypt the double AES encryption"""
    try:
        # Second decryption (reverse order)
        key2 = k4 + k3
        cipher2 = AES.new(key2, mode=AES.MODE_ECB)
        intermediate = cipher2.decrypt(ciphertext)
        
        # First decryption
        key1 = k1 + k2
        cipher1 = AES.new(key1, mode=AES.MODE_ECB)
        plaintext = cipher1.decrypt(intermediate)
        
        # Try to unpad
        return unpad(plaintext, 16)
    except Exception as e:
        return None

def main():
    # Read the output
    with open('out.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    example_ct = bytes.fromhex(lines[0])
    flag_ct = bytes.fromhex(lines[1])
    
    print("Reproducing keys...")
    k1, k2, k3, k4 = reproduce_exact_keys()
    
    print(f"k1: {k1.hex()}")
    print(f"k2: {k2.hex()}")
    print(f"k3: {k3.hex()}")
    print(f"k4: {k4.hex()}")
    
    # Test with known plaintext
    known_plaintext = b"example"
    decrypted = decrypt_double_aes(example_ct, k1, k2, k3, k4)
    
    if decrypted == known_plaintext:
        print("Keys verified with known plaintext!")
        
        # Decrypt the flag
        flag = decrypt_double_aes(flag_ct, k1, k2, k3, k4)
        if flag:
            print(f"Flag: {flag.decode()}")
        else:
            print("Failed to decrypt flag")
    else:
        print(f"Key verification failed. Got: {decrypted}")

if __name__ == "__main__":
    main()
