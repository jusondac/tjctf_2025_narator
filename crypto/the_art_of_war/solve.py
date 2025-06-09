#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
import re

# Try to import gmpy2 for faster arithmetic
try:
    import gmpy2
    HAS_GMPY2 = True
    print("Using gmpy2 for faster arithmetic")
except ImportError:
    HAS_GMPY2 = False
    print("gmpy2 not available, using Python's built-in arithmetic")

def parse_output(filename):
    """Parse the output file to extract e, n values, and c values"""
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract e
    e_match = re.search(r'e = (\d+)', content)
    e = int(e_match.group(1))
    
    # Extract n values
    n_matches = re.findall(r'n(\d+) = (\d+)', content)
    n_values = {}
    for i, n in n_matches:
        n_values[int(i)] = int(n)
    
    # Extract c values  
    c_matches = re.findall(r'c(\d+) = (\d+)', content)
    c_values = {}
    for i, c in c_matches:
        c_values[int(i)] = int(c)
    
    return e, n_values, c_values

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def chinese_remainder_theorem(remainders, moduli):
    """
    Solve system of congruences using Chinese Remainder Theorem
    x ≡ remainders[i] (mod moduli[i])
    """
    if len(remainders) != len(moduli):
        raise ValueError("Number of remainders and moduli must be equal")
    
    # Calculate the product of all moduli
    N = 1
    for m in moduli:
        N *= m
    
    result = 0
    for i in range(len(remainders)):
        # Calculate N_i = N / moduli[i]
        N_i = N // moduli[i]
        
        # Find the modular inverse of N_i mod moduli[i]
        gcd, M_i, _ = extended_gcd(N_i, moduli[i])
        if gcd != 1:
            raise ValueError(f"Moduli are not pairwise coprime: gcd({N_i}, {moduli[i]}) = {gcd}")
        
        # Add to result
        result += remainders[i] * N_i * M_i
    
    return result % N

def nth_root(n, k):
    """Calculate the k-th root of n using a more efficient method"""
    if k == 1:
        return n
    if k == 2:
        # Use integer square root
        if n == 0:
            return 0
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x
    
    # For higher roots, use binary search with optimized bounds
    if n < 2:
        return n
    
    # Better initial bounds
    low = 1
    high = 1
    while high ** k < n:
        high *= 2
    
    # Binary search with early termination
    while low <= high:
        mid = (low + high) // 2
        mid_k = mid ** k
        
        if mid_k == n:
            return mid
        elif mid_k < n:
            low = mid + 1
        else:
            high = mid - 1
    
    return high

def solve_hastad_attack():
    """Solve using Håstad's Broadcast Attack"""
    
    # Parse the output file
    e, n_values, c_values = parse_output('output.txt')
    
    print(f"Found e = {e}")
    print(f"Found {len(n_values)} moduli")
    print(f"Found {len(c_values)} ciphertexts")
    
    # Try with different subset sizes, starting small
    for subset_size in [3, 5, 10, 20, 50, min(100, e), e]:
        print(f"\nTrying with {subset_size} equations...")
        
        # Prepare data for CRT
        remainders = []
        moduli = []
        
        # Use the first subset_size equations
        for i in range(min(subset_size, e)):
            if i in c_values and i in n_values:
                remainders.append(c_values[i])
                moduli.append(n_values[i])
            else:
                print(f"Missing data for index {i}")
                break
        
        if len(remainders) < subset_size:
            continue
            
        print(f"Using {len(remainders)} equations for CRT")
        
        try:
            # Apply Chinese Remainder Theorem
            print("Applying Chinese Remainder Theorem...")
            m_e = chinese_remainder_theorem(remainders, moduli)
            
            # Take the e-th root
            print(f"Taking the {len(remainders)}-th root...")
            m = nth_root(m_e, len(remainders))
            
            # Verify the result by checking if m^e matches one of the ciphertexts
            if pow(m, e, moduli[0]) == remainders[0]:
                print("Root verification successful!")
                
                # Convert to bytes and check if it's a valid flag
                try:
                    flag = long_to_bytes(m)
                    print(f"Recovered message: {flag}")
                    
                    # Check if it looks like a flag
                    if b'tjctf{' in flag or b'flag{' in flag or flag.startswith(b'tjctf{'):
                        print(f"SUCCESS! Flag: {flag.decode('ascii', errors='ignore')}")
                        return flag
                    elif flag.isprintable():
                        print(f"Printable result: {flag}")
                        # Continue trying with more equations
                        
                except Exception as e:
                    print(f"Error converting to bytes: {e}")
            else:
                print("Root verification failed, trying with more equations...")
                
        except Exception as ex:
            print(f"Error with {subset_size} equations: {ex}")
            continue
    
    print("Failed to recover the flag with all attempted subset sizes")
    return None

if __name__ == "__main__":
    solve_hastad_attack()
