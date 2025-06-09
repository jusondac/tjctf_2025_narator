import numpy as np

def decode_dude(filename="dude.txt"):
    """
    Decode the flag from a file using known plaintext attack
    """
    # Read the encoded data
    with open(filename, "r") as f:
        lines = f.readlines()
    
    # Parse the encoded matrix (these are large integers, not binary)
    encoded_data = []
    for line in lines:
        if line.strip():
            row = list(map(float, line.strip().split()))
            encoded_data.append(row)
    
    encoded_matrix = np.array(encoded_data, dtype=float)
    print(f"Loaded encoded matrix: {encoded_matrix.shape}")
    
    # Known filler text (exactly as in encode.py)
    filler = "In cybersecurity, a CTF (Capture The Flag) challenge is a competitive, gamified event where participants, either individually or in teams, are tasked with finding and exploiting vulnerabilities in systems to capture hidden information known as flags. These flags are typically used to score points. CTFs test skills in areas like cryptography, web security, reverse engineering, and forensics, offering an exciting way to learn, practice, and showcase cybersecurity expertise.  This flag is for you: "
    
    n = 64  # Block size from encode.py
    
    # Convert filler to binary (exactly as in encode.py)
    filler_binary = "".join([bin(ord(i))[2:].zfill(8) for i in filler])
    print(f"Filler: {len(filler)} chars -> {len(filler_binary)} bits")
    
    # Pad the filler binary exactly as in encode.py
    filler_binary_padded = filler_binary + "0" * (n - len(filler_binary) % n)
    print(f"Filler padded: {len(filler_binary_padded)} bits")
    
    # Create known plaintext blocks
    known_blocks = []
    for i in range(0, len(filler_binary_padded), n):
        if i + n <= len(filler_binary_padded):
            block = [int(b) for b in filler_binary_padded[i:i+n]]
            known_blocks.append(block)
    
    known_matrix = np.array(known_blocks, dtype=float)
    print(f"Known filler blocks: {known_matrix.shape}")
    
    # Use the corresponding encoded blocks for key recovery
    num_known = len(known_blocks)
    if num_known > len(encoded_matrix):
        print(f"Error: Need at least {num_known} encoded blocks, but only have {len(encoded_matrix)}")
        return None
        
    encoded_subset = encoded_matrix[:num_known]
    print(f"Using first {num_known} encoded blocks for key recovery")
    
    try:
        # Recover the key using known plaintext attack
        # From encode.py: plaintext_row @ key = encoded_row
        # So: known_matrix @ key = encoded_subset
        key, residuals, rank, s = np.linalg.lstsq(known_matrix, encoded_subset, rcond=None)
        
        print(f"Key recovery - Matrix rank: {rank}/{min(known_matrix.shape)}")
        print(f"Key matrix shape: {key.shape}")
        
        # Decode all blocks using the recovered key
        print(f"Decoding all {len(encoded_matrix)} blocks...")
        
        all_decoded_bits = []
        successful_blocks = 0
        
        for block_idx, encoded_row in enumerate(encoded_matrix):
            try:
                # Solve: plaintext_row @ key = encoded_row
                # So: plaintext_row = solve(key.T, encoded_row)
                decoded_row, _, _, _ = np.linalg.lstsq(key.T, encoded_row, rcond=None)
                
                # Convert to binary bits
                binary_block = []
                for val in decoded_row:
                    binary_block.append(1 if val > 0.5 else 0)
                
                all_decoded_bits.extend(binary_block)
                successful_blocks += 1
                
            except Exception as e:
                print(f"Failed to decode block {block_idx}: {e}")
                all_decoded_bits.extend([0] * n)
        
        print(f"Successfully decoded {successful_blocks}/{len(encoded_matrix)} blocks")
        
        # Convert bits to text
        decoded_text = ""
        for i in range(0, len(all_decoded_bits), 8):
            if i + 8 <= len(all_decoded_bits):
                byte_bits = all_decoded_bits[i:i+8]
                byte_val = int("".join(map(str, byte_bits)), 2)
                
                # Include printable ASCII characters
                if 32 <= byte_val <= 126:
                    decoded_text += chr(byte_val)
                elif byte_val in [10, 9]:  # newline, tab
                    decoded_text += chr(byte_val)
        
        print(f"Decoded text length: {len(decoded_text)} characters")
        print("\nDecoded text:")
        print("="*60)
        print(decoded_text)
        print("="*60)
        
        # Extract the flag part (after filler)
        if filler in decoded_text:
            flag_part = decoded_text.split(filler, 1)[1]
            print(f"\nFlag part: {repr(flag_part)}")
            return flag_part.strip()
        else:
            # Look for partial patterns
            patterns = ["f{", "ctf{", "jctf{", "tctf{", "tjctf{"]
            for pattern in patterns:
                if pattern in decoded_text:
                    flag_start = decoded_text.find(pattern)
                    flag_section = decoded_text[flag_start:]
                    # Clean up the flag section
                    clean_flag = ""
                    for c in flag_section:
                        if c.isprintable() and c not in ['\t', '\n']:
                            clean_flag += c
                    
                    if pattern == "f{":
                        complete_flag = "tjct" + clean_flag
                    elif pattern == "ctf{":
                        complete_flag = "tj" + clean_flag
                    elif pattern == "jctf{":
                        complete_flag = "t" + clean_flag
                    else:
                        complete_flag = clean_flag
                    
                    # Add closing brace if missing
                    if "}" not in complete_flag:
                        complete_flag += "}"
                    
                    print(f"\n🔍 Found pattern '{pattern}': {clean_flag}")
                    print(f"🎯 Reconstructed flag: {complete_flag}")
                    return complete_flag
        
        return None
        
    except Exception as e:
        print(f"Error during decoding: {e}")
        import traceback
        traceback.print_exc()
        return None

print(decode_dude())