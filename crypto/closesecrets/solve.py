#!/usr/bin/env python3
import hashlib
from ast import literal_eval

def decrypt_outer(cipher_ords, key):
    """Reverse the outer encryption layer"""
    plaintext_ords = []
    key_offset = key % 256
    for val in cipher_ords:
        # Reverse: (val + key_offset) * key = cipher_val
        # So: val = (cipher_val / key) - key_offset
        decrypted_val = (val // key) - key_offset
        plaintext_ords.append(decrypted_val)
    return plaintext_ords

def decrypt_xor(encrypted_ords, text_key_bytes):
    """Reverse the XOR encryption (same operation as encryption)"""
    decrypted_bytes = []
    key_length = len(text_key_bytes)
    for i, ord_val in enumerate(encrypted_ords):
        key_byte = text_key_bytes[i % key_length]
        decrypted_bytes.append(ord_val ^ key_byte)
    # Reverse the byte order since original was reversed with [::-1]
    return bytes(decrypted_bytes[::-1])

def solve():
    # Read parameters
    with open("params.txt", "r") as f:
        lines = f.readlines()
        p = int(lines[0].split(" = ")[1].strip())
        g = int(lines[1].split(" = ")[1].strip())
        u = int(lines[2].split(" = ")[1].strip())
        v = int(lines[3].split(" = ")[1].strip())
    
    # Read encrypted flag
    with open("enc_flag", "r") as f:
        cipher_text = f.read().strip()
        final_cipher = literal_eval(cipher_text)
    
    print(f"p = {p}")
    print(f"g = {g}")
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"Cipher length: {len(final_cipher)}")
    
    # The vulnerability: a is in range [p-10, p] and b is in range [g-10, g]
    # We can brute force these small ranges
    
    print("Brute forcing private keys...")
    
    for a in range(p - 10, p + 1):
        if pow(g, a, p) == u:
            print(f"Found a = {a}")
            break
    else:
        print("Could not find a")
        return
    
    for b in range(g - 10, g + 1):
        if pow(g, b, p) == v:
            print(f"Found b = {b}")
            break
    else:
        print("Could not find b")
        return
    
    # Calculate shared key
    shared_key = pow(v, a, p)
    print(f"Shared key = {shared_key}")
    
    # Verify the key is correct
    b_key = pow(u, b, p)
    if shared_key != b_key:
        print("Key verification failed!")
        return
    
    print("Key verification successful!")
    
    # Decrypt the flag
    # First, reverse the outer encryption
    intermediate_ords = decrypt_outer(final_cipher, shared_key)
    print(f"Intermediate ords length: {len(intermediate_ords)}")
    
    # Generate XOR key
    xor_key_str = hashlib.sha256(str(shared_key).encode()).hexdigest()
    xor_key_bytes = xor_key_str.encode('utf-8')
    print(f"XOR key: {xor_key_str}")
    
    # Reverse the XOR encryption
    flag_bytes = decrypt_xor(intermediate_ords, xor_key_bytes)
    
    try:
        flag = flag_bytes.decode('utf-8')
        print(f"Flag: {flag}")
    except UnicodeDecodeError:
        print("Failed to decode flag as UTF-8")
        print(f"Raw bytes: {flag_bytes}")

if __name__ == "__main__":
    solve()
# Flag: tjctf{sm4ll_r4ng3_sh0rt_s3cr3t}