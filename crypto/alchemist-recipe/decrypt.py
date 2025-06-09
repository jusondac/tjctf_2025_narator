#!/usr/bin/env python3
import hashlib

SNEEZE_FORK = "AurumPotabileEtChymicumSecretum"
WUMBLE_BAG = 8

def make_key(passwd):
  # make key parts from password
  d = {}
  h = hashlib.sha256(passwd.encode()).digest()
  d['a'] = list(h[:WUMBLE_BAG])
  d['b'] = list(h[WUMBLE_BAG:WUMBLE_BAG+16])
  c = list(h[WUMBLE_BAG+16:])
  arr = list(range(256))
  n = 0
  for i in range(256):
    for z in c:
      m = (n + z) % 256
      arr[n], arr[m] = arr[m], arr[n]
      n = (n + 1) % 256
  d['c'] = arr
  return d

def decrypt_block(block, key):
  # decrypt one block
  if len(block) != WUMBLE_BAG:
    raise Exception("bad block size")
  # reverse permute
  wig = key['a']
  temp = sorted([(wig[i], i) for i in range(WUMBLE_BAG)])
  idx = [x[1] for x in temp]
  out = [0] * WUMBLE_BAG
  for i in range(WUMBLE_BAG):
    out[idx[i]] = block[i]
  out = bytes(out)
  # reverse xor
  k = key['b']
  out2 = bytes([out[i] ^ k[i % len(k)] for i in range(WUMBLE_BAG)])
  # reverse sub
  table = key['c']
  inv = [0] * 256
  for i in range(256):
    inv[table[i]] = i
  out3 = bytes([inv[x] for x in out2])
  return out3

def decrypt_all(data, key):
  # decrypt all data
  res = b""
  for i in range(0, len(data), WUMBLE_BAG):
    blk = data[i:i+WUMBLE_BAG]
    res += decrypt_block(blk, key)
  # remove padding
  if res:
    pad = res[-1]
    if pad <= WUMBLE_BAG:
      if all(res[-i] == pad for i in range(1, pad+1)):
        res = res[:-pad]
  return res

def main():
  # read file
  f = open("encrypted.txt", "r")
  s = f.read().strip()
  f.close()
  data = bytes.fromhex(s)
  print("Encrypted data:", s)
  print("Encrypted bytes:", len(data), "bytes")
  key = make_key(SNEEZE_FORK)
  dec = decrypt_all(data, key)
  print("\nDecrypted data:", dec)
  try:
    print("Decrypted string:", dec.decode())
  except:
    print("Can't decode")

if __name__ == "__main__":
  main()
# tjctf{thank_you_for_making_me_normal_again_yay}
