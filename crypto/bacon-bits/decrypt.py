#!/usr/bin/env python3

# Read the encrypted text from file
with open('out.txt', 'r') as f:
  encrypted_text = f.read().strip()

# Reverse Caesar shift (+13)
decrypted_text = ''
for char in encrypted_text:
  decrypted_text += chr(ord(char) + 13)

# Make Baconian cipher mapping
baconian = {
  '00000': 'a', '00001': 'b', '00010': 'c', '00011': 'd',
  '00100': 'e', '00101': 'f', '00110': 'g', '00111': 'h',
  '01000': 'i', '01001': 'k', '01010': 'l', '01011': 'm',
  '01100': 'n', '01101': 'o', '01110': 'p', '01111': 'q',
  '10000': 'r', '10001': 's', '10010': 't', '10011': 'u',
  '10100': 'w', '10101': 'x', '10110': 'y', '10111': 'z'
}

# Get binary string from case (upper=1, lower=0)
binary = ''
for c in decrypted_text:
  if c.isupper():
    binary += '1'
  else:
    binary += '0'

# Decode 5 bits at a time
flag = ''
for i in range(0, len(binary), 5):
  chunk = binary[i:i+5]
  if len(chunk) == 5:
    if chunk in baconian:
      flag += baconian[chunk]
    else:
      flag += '?'

print(flag)
