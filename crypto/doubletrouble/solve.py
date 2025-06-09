#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import itertools

def get_deterministic_parts():
    """Get the deterministic parts k1, k3 and choices"""
    myrandom = random.Random(42)
    k1 = myrandom.randbytes(8)
    choices = list(myrandom.randbytes(6))
    # it took forever, so we just use the first 4 choices for k2
    # For k3, k4 - start fresh with same seed``
    myrandom2 = random.Random(42)
    k3 = myrandom2.randbytes(8)
    choices2 = list(myrandom2.randbytes(6))
    
    return k1, k3, choices, choices2

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
    except:
        return None

def main():
    # Read the output
    with open('out.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    example_ct = bytes.fromhex(lines[0])
    flag_ct = bytes.fromhex(lines[1])
    
    # Get deterministic parts
    k1, k3, choices1, choices2 = get_deterministic_parts()
    
    print(f"k1: {k1.hex()}")
    print(f"k3: {k3.hex()}")
    print(f"choices1: {[hex(c) for c in choices1]}")
    print(f"choices2: {[hex(c) for c in choices2]}")
    
    known_plaintext = b"example"
    
    print("Using meet-in-the-middle attack...")
    print("First, finding all possible intermediate values by trying all k2 values...")
    
    # Meet-in-the-middle: First encrypt with all possible k1+k2, store results
    intermediate_map = {}
    
    count = 0
    for k2_indices in itertools.product(range(4), repeat=8):
        k2 = bytes([choices1[i] for i in k2_indices])
        count += 1
        
        if count % 10000 == 0:
            print(f"Processed {count:,} k2 combinations...")
            
        try:
            # First encryption: plaintext -> intermediate
            key1 = k1 + k2
            cipher1 = AES.new(key1, mode=AES.MODE_ECB)
            intermediate = cipher1.encrypt(pad(known_plaintext, 16))
            intermediate_map[intermediate] = k2
        except:
            continue
    
    print(f"Generated {len(intermediate_map)} intermediate values")
    print("Now trying all k4 values to see if we can decrypt to one of these intermediates...")
    
    count = 0
    for k4_indices in itertools.product(range(4), repeat=8):
        k4 = bytes([choices2[i] for i in k4_indices])
        count += 1
        
        if count % 10000 == 0:
            print(f"Processed {count:,} k4 combinations...")
            
        try:
            # Second decryption: ciphertext -> intermediate
            key2 = k4 + k3
            cipher2 = AES.new(key2, mode=AES.MODE_ECB)
            intermediate = cipher2.decrypt(example_ct)
            
            # Check if this intermediate matches any from our map
            if intermediate in intermediate_map:
                k2 = intermediate_map[intermediate]
                print(f"SUCCESS! Found matching keys!")
                print(f"k1: {k1.hex()}")
                print(f"k2: {k2.hex()}")
                print(f"k3: {k3.hex()}")
                print(f"k4: {k4.hex()}")
                
                # Verify with full decryption
                decrypted = decrypt_double_aes(example_ct, k1, k2, k3, k4)
                if decrypted == known_plaintext:
                    print("Verification successful!")
                    
                    # Decrypt the flag
                    flag = decrypt_double_aes(flag_ct, k1, k2, k3, k4)
                    if flag:
                        print(f"Flag: {flag.decode()}")
                        return
                    else:
                        print("Failed to decrypt flag")
                        return
                else:
                    print(f"Verification failed: {decrypted}")
        except:
            continue
    
    print("Meet-in-the-middle attack failed")

if __name__ == "__main__":
    main()
