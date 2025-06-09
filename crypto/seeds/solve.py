#!/usr/bin/env python3

import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timezone, timedelta

class RandomGenerator:
    def __init__(self, seed = None, modulus = 2 ** 32, multiplier = 157, increment = 1):
        if seed is None: 
            seed = time.asctime()
        if type(seed) is int: 
            self.seed = seed
        if type(seed) is str: 
            self.seed = int.from_bytes(seed.encode(), "big")
        if type(seed) is bytes: 
            self.seed = int.from_bytes(seed, "big")
        self.m = modulus
        self.a = multiplier
        self.c = increment

    def randint(self, bits: int):
        self.seed = (self.a * self.seed + self.c) % self.m
        result = self.seed.to_bytes(4, "big")
        while len(result) < bits // 8:
            self.seed = (self.a * self.seed + self.c) % self.m
            result += self.seed.to_bytes(4, "big")
        return int.from_bytes(result, "big") % (2 ** bits)

    def randbytes(self, len: int):
        return self.randint(len * 8).to_bytes(len, "big")

def get_flag_ciphertext():
    """Get the flag ciphertext from the provided server response"""
    # From the server response we got:
    ciphertext_bytes = b'I<B\x8f7\x1a\x9d\xba\xcb=Dz8\x97\xe9c\xb7\xaf\x15\x01\xf4\xd9\xd9\xc2\x83jm\x1a\xa2\xda\x10\xb5'
    print(f"Flag ciphertext: {ciphertext_bytes.hex()}")
    return ciphertext_bytes

def generate_possible_seeds():
    """Generate possible seed strings based on US Eastern time"""
    # US Eastern timezone (UTC-5 in standard time, UTC-4 in daylight time)
    # Since it's June 8, 2025, it should be daylight saving time (EDT = UTC-4)
    eastern_tz = timezone(timedelta(hours=-4))
    
    # Get current time in Eastern timezone
    now_eastern = datetime.now(eastern_tz)
    
    # Generate possible asctime() strings for the current time and nearby times
    # asctime() format: "Day Mon DD HH:MM:SS YYYY"
    possible_seeds = []
    
    # Try current time and a few minutes before/after to account for network delay
    for offset in range(-300, 301):  # 5 minutes before and after
        test_time = now_eastern + timedelta(seconds=offset)
        # Convert to time.struct_time and then to asctime format
        time_tuple = test_time.timetuple()
        asctime_str = time.asctime(time_tuple)
        possible_seeds.append(asctime_str)
    
    return possible_seeds

def try_decrypt_flag(ciphertext, possible_seeds):
    """Try to decrypt the flag using possible seeds"""
    for seed_str in possible_seeds:
        try:
            # Create RNG with the seed
            rng = RandomGenerator(seed_str)
            
            # Generate the same key as used for the flag
            key = rng.randbytes(32)
            
            # Try to decrypt
            cipher = AES.new(key, AES.MODE_ECB)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            
            # Check if it looks like a flag
            if b'tjctf{' in plaintext or b'flag' in plaintext.lower():
                print(f"Found flag with seed: {seed_str}")
                print(f"Flag: {plaintext.decode()}")
                return plaintext.decode()
                
        except Exception as e:
            # Invalid padding or other error, try next seed
            continue
    
    return None

def main():
    print("Solving seeds challenge...")
    
    # Get flag ciphertext from the known server response
    flag_ciphertext = get_flag_ciphertext()
    
    # Generate possible seeds
    print("Generating possible seeds...")
    possible_seeds = generate_possible_seeds()
    print(f"Generated {len(possible_seeds)} possible seeds")
    
    # Try to decrypt the flag
    print("Trying to decrypt flag...")
    flag = try_decrypt_flag(flag_ciphertext, possible_seeds)
    
    if flag:
        print(f"Success! Flag: {flag}")
    else:
        print("Failed to decrypt flag. The seed might be outside our time range.")
        print("First few seeds tried:")
        for i, seed in enumerate(possible_seeds[:5]):
            print(f"  {i+1}: {seed}")

if __name__ == "__main__":
    main()
