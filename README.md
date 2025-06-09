# TJCTF CTF Challenges Workspace

This repository contains a collection of CTF challenges from TJCTF, organized by category. Each challenge includes source files, solutions, and where applicable, solved flags.

## 📁 Directory Structure

```
├── crypto/          # Cryptography challenges
├── misc/           # Miscellaneous challenges  
├── pwn/            # Binary exploitation challenges
└── README.md       # This file
```

---

## 🔐 Cryptography Challenges

### [alchemist-recipe](./crypto/alchemist-recipe/)
**Description:** An alchemist claims to have a recipe to transform lead into gold, but accidentally encrypted it with a peculiar process. He left behind notes on the encryption method and an encrypted sample, but spilled magic ink making them weirdly formatted.

**Files:**
- [`challenges.txt`](./crypto/alchemist-recipe/challenges.txt) - Challenge description
- [`chall.py`](./crypto/alchemist-recipe/chall.py) - Challenge source code
- [`encrypted.txt`](./crypto/alchemist-recipe/encrypted.txt) - Encrypted flag
- [`decrypt.py`](./crypto/alchemist-recipe/decrypt.py) - Solution script
- **Flag:** `tjctf{thank_you_for_making_me_normal_again_yay}`

### [bacon-bits](./crypto/bacon-bits/)
**Description:** A cipher challenge involving Bacon cipher encryption.

**Files:**
- [`enc.py`](./crypto/bacon-bits/enc.py) - Encryption script
- [`out.txt`](./crypto/bacon-bits/out.txt) - Encrypted output
- [`decrypt.py`](./crypto/bacon-bits/decrypt.py) - Solution script

### [closesecrets](./crypto/closesecrets/)
**Description:** A custom Diffie-Hellman implementation that went too far. Can you make sense of this custom cryptography and decode the encrypted flag?

**Files:**
- [`closesecrets.txt`](./crypto/closesecrets/closesecrets.txt) - Challenge description
- [`encrypt.py`](./crypto/closesecrets/encrypt.py) - Encryption implementation
- [`params.txt`](./crypto/closesecrets/params.txt) - Encryption parameters
- [`enc_flag`](./crypto/closesecrets/enc_flag) - Encrypted flag
- [`solve.py`](./crypto/closesecrets/solve.py) - Solution script
- **Flag:** `tjctf{sm4ll_r4ng3_sh0rt_s3cr3t}`

### [dotdotdotv2](./crypto/dotdotdotv2/)
**Description:** A challenge involving numpy dot operations. Hint: "might wanna find out what np . dot does first..."

**Files:**
- [`dotdotdotv2.txt`](./crypto/dotdotdotv2/dotdotdotv2.txt) - Challenge hint
- [`encode.py`](./crypto/dotdotdotv2/encode.py) - Encoding script
- [`dude.txt`](./crypto/dotdotdotv2/dude.txt) - Encoded data (large numeric sequences)
- [`encoded.txt`](./crypto/dotdotdotv2/encoded.txt) - Additional encoded data
- [`decoder.py`](./crypto/dotdotdotv2/decoder.py) - Solution script
- [`fake_flag.txt`](./crypto/dotdotdotv2/fake_flag.txt) - Test flag

### [doubletrouble](./crypto/doubletrouble/)
**Description:** "Twice the encryption, half the security" - A challenge involving double encryption.

**Files:**
- [`doubletrouble.txt`](./crypto/doubletrouble/doubletrouble.txt) - Challenge description
- [`enc.py`](./crypto/doubletrouble/enc.py) - Encryption script
- [`out.txt`](./crypto/doubletrouble/out.txt) - Encrypted output
- [`solve.py`](./crypto/doubletrouble/solve.py) - Solution script
- [`solve_optimized.py`](./crypto/doubletrouble/solve_optimized.py) - Optimized solution

### [seeds](./crypto/seeds/)
**Description:** "You can't grow crops without planting the seeds" - A challenge involving random number generation seeded with time.

**Files:**
- [`seeds.txt`](./crypto/seeds/seeds.txt) - Challenge description
- [`main.py`](./crypto/seeds/main.py) - Challenge server code
- [`solve.py`](./crypto/seeds/solve.py) - Solution script
- **Server:** `nc tjc.tf 31493` (US Eastern time zone)

### [the_art_of_war](./crypto/the_art_of_war/)
**Description:** "In the midst of chaos, there is also opportunity" - Sun Tzu, The Art of War. A cryptographic challenge involving multiple RSA encryptions.

**Files:**
- [`theartofwar.txt`](./crypto/the_art_of_war/theartofwar.txt) - Challenge description/quote
- [`main.py`](./crypto/the_art_of_war/main.py) - Challenge implementation
- [`output.txt`](./crypto/the_art_of_war/output.txt) - Multiple RSA ciphertext pairs
- [`solve.py`](./crypto/the_art_of_war/solve.py) - Solution script

---

## 🎯 Miscellaneous Challenges

### [golfhardester](./misc/golfhardester/)
**Description:** A regex code golf challenge - "you guys were definitely missing regex golfing this year... right?"

**Files:**
- [`golfharderster.txt`](./misc/golfhardester/golfharderster.txt) - Challenge description
- [`golf.py`](./misc/golfhardester/golf.py) - Challenge script
- [`match.txt`](./misc/golfhardester/match.txt) - Test cases and expected matches
- [`solve.py`](./misc/golfhardester/solve.py) - Solution script
- [`solved challenge.txt`](./misc/golfhardester/solved%20challenge.txt) - Solution notes
- **Flag:** `tjctf{davidebyzero_is_my_hero_6a452cbdc75f}`
- **Server:** `nc tjc.tf 31132`

### [make_group](./misc/make_group/)
**Description:** A mathematical challenge involving large number calculations.

**Files:**
- [`chall.txt`](./misc/make_group/chall.txt) - Contains the number `500000`
- [`calc.py`](./misc/make_group/calc.py) - Solution calculation script
- [`flag.sh`](./misc/make_group/flag.sh) - Flag generation script

### [mouse_trail](./misc/mouse_trail/)
**Description:** A number guessing game with mouse movement tracking.

**Files:**
- [`chall.py`](./misc/mouse_trail/chall.py) - Challenge server (guess number 1-1000)
- [`mouse_movements.txt`](./misc/mouse_trail/mouse_movements.txt) - Mouse movement data
- [`mouse.py`](./misc/mouse_trail/mouse.py) - Mouse tracking analysis

---

## 💥 PWN (Binary Exploitation) Challenges

### [buggy](./pwn/buggy/)
**Description:** "I HATE bugs in production." - Buffer overflow challenge.

**Files:**
- [`challenge.txt`](./pwn/buggy/challenge.txt) - Challenge description
- [`chall`](./pwn/buggy/chall) - Binary executable
- [`chall.c`](./pwn/buggy/chall.c) - Source code
- [`exploit.py`](./pwn/buggy/exploit.py) - Working exploit
- [`objdump_buggy.txt`](./pwn/buggy/objdump_buggy.txt) - Disassembly
- **Flag:** `tjctf{up_up_d0wn_d0wn_l3ft_r1ght_l3ft_r1ght_b_a}`
- **Server:** `nc tjc.tf 31363`

### [city-planning](./pwn/city-planning/)
**Description:** "I'm building a new city but I need help with the design process"

**Files:**
- [`challenges.txt`](./pwn/city-planning/challenges.txt) - Challenge description
- [`chall`](./pwn/city-planning/chall) - Binary executable
- [`chall.c`](./pwn/city-planning/chall.c) - Source code
- [`exploit_final.py`](./pwn/city-planning/exploit_final.py) - Working exploit
- **Server:** `nc tjc.tf 31489`

### [extra-credit](./pwn/extra-credit/)
**Description:** "Agent P, could you please take a look at our internal grading system? I really don't want to get rescinded..."

**Files:**
- [`challenges.txt`](./pwn/extra-credit/challenges.txt) - Challenge description
- [`gradeViewer`](./pwn/extra-credit/gradeViewer) - Binary executable
- [`gradeViewer.c`](./pwn/extra-credit/gradeViewer.c) - Source code
- [`exploit.py`](./pwn/extra-credit/exploit.py) - Local exploit
- [`nc_exploit.py`](./pwn/extra-credit/nc_exploit.py) - Remote exploit
- **Flag:** `tjctf{th4nk_y0u_f0r_sav1ng_m3y_grade}`
- **Server:** `nc tjc.tf 31624`

### [i-love-bird](./pwn/i-love-bird/)
**Description:** A bird-themed binary exploitation challenge.

**Files:**
- [`url.txt`](./pwn/i-love-bird/url.txt) - Server connection info
- [`birds`](./pwn/i-love-bird/birds) - Binary executable
- [`birds.c`](./pwn/i-love-bird/birds.c) - Source code
- [`exploit.py`](./pwn/i-love-bird/exploit.py) - Working exploit
- **Flag:** `tjctf{1_gu355_y0u_f0und_th3_f4ke_b1rd_ch1rp_CH1rp_cH1Rp_Ch1rP_ch1RP}`
- **Server:** `nc tjc.tf 31625`

### [linked](./pwn/linked/)
**Description:** A linked list data structure exploitation challenge.

**Files:**
- [`chall`](./pwn/linked/chall) - Binary executable
- [`chall.c`](./pwn/linked/chall.c) - Source code
- [`exploit.py`](./pwn/linked/exploit.py) - Working exploit
- [`Dockerfile`](./pwn/linked/Dockerfile) - Container setup
- [`libc.so.6`](./pwn/linked/libc.so.6) - Libc library
- **Flag:** `tjctf{i_h0pe_my_tre3s_ar3nt_b4d_too}`

### [wrong-warp](./pwn/wrong-warp/)
**Description:** "Credits warps sure are cool in speedrunning" - A game-themed exploitation challenge.

**Files:**
- [`challenge.txt`](./pwn/wrong-warp/challenge.txt) - Challenge description
- [`heroQuest`](./pwn/wrong-warp/heroQuest) - Binary executable
- [`exploit.py`](./pwn/wrong-warp/exploit.py) - Local exploit
- [`exploit_remote.py`](./pwn/wrong-warp/exploit_remote.py) - Remote exploit
- [`objdump_heroquest.txt`](./pwn/wrong-warp/objdump_heroquest.txt) - Disassembly
- [`flag.txt`](./pwn/wrong-warp/flag.txt) - Test flag
- **Flag:** `tjctf{up_up_d0wn_d0wn_l3ft_r1ght_l3ft_r1ght_b_a}`
- **Server:** `nc tjc.tf 31365`

---

## 🏆 Solved Flags Summary

| Category | Challenge | Flag |
|----------|-----------|------|
| Crypto | alchemist-recipe | `tjctf{thank_you_for_making_me_normal_again_yay}` |
| Crypto | closesecrets | `tjctf{sm4ll_r4ng3_sh0rt_s3cr3t}` |
| Misc | golfhardester | `tjctf{davidebyzero_is_my_hero_6a452cbdc75f}` |
| PWN | buggy | `tjctf{up_up_d0wn_d0wn_l3ft_r1ght_l3ft_r1ght_b_a}` |
| PWN | extra-credit | `tjctf{th4nk_y0u_f0r_sav1ng_m3y_grade}` |
| PWN | i-love-bird | `tjctf{1_gu355_y0u_f0und_th3_f4ke_b1rd_ch1rp_CH1rp_cH1Rp_Ch1rP_ch1RP}` |
| PWN | linked | `tjctf{i_h0pe_my_tre3s_ar3nt_b4d_too}` |
| PWN | wrong-warp | `tjctf{up_up_d0wn_d0wn_l3ft_r1ght_l3ft_r1ght_b_a}` |

---

## 🛠️ Tools & Resources

- **Python scripts** for cryptography challenges
- **Binary analysis tools** for PWN challenges
- **Exploit development** with pwntools
- **Mathematical solvers** for algorithmic challenges

## 📝 Notes

- Most PWN challenges include both local and remote exploits
- Crypto challenges often include both encoding and decoding scripts
- Several challenges have working solutions with confirmed flags
- Server connections use `nc tjc.tf <port>` format
- Challenges span various difficulty levels and techniques

---

*This README was generated by scanning all files in the TJCTF workspace and analyzing challenge descriptions, source code, and solution scripts.*
