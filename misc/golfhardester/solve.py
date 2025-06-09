import regex

re = r'''(?x)
# Want to check if the string has equal counts of all the unique characters
#
# <a> = 1
# <big_loop> = 2
# <b> = 4
# <main_loop> = 5

# Capture first character; we will test everything against it
^
(?<a>.)

(
    \g<a>|  # Skip matching a character against itself

    # Capture next character to test against the first
    (?<b>.)
    (?=
    # Goto end of string
    .*$
        (?<=

        # Test if chars in \g<a> and \g<b> have same counts in the string
        ^
        (?<main_loop>
            (?!\g<a>|\g<b>).  # skip
            |\g<a>(?&main_loop)*?\g<b>
            |\g<b>(?&main_loop)*?\g<a>
        )*

        )
    )
)*$
'''

# strip down re
re = regex.sub(r'#.*', '', re)  # remove comments
re = regex.sub(r'\s+', '', re)  # remove whitespace
if re.startswith('(?x)'):
    re = re[4:]  # remove (?x) if present
re = re.replace('?<a>', '').replace('\\g<a>', '\\1')
# re = re.replace('?<big_loop>', '').replace('&big_loop', '2')
re = re.replace('?<b>', '').replace('\\g<b>', '\\3')
re = re.replace('?<main_loop>', '').replace('&main_loop', '4')

print(len(re), re)
re = regex.compile(re, regex.V1)

case = 'pullup'
match = re.search(case)
print(match, match.groups() if match is not None else None)
print(case.count('b'), case.count('c'), len(case))

match = open('match.txt').read().splitlines()
nonmatch = open('nonmatch.txt').read().splitlines()
for m in match:
    if not re.search(m):
        print(f'Failed match: {m}', len(m))
for m in nonmatch:
    if re.search(m):
        print(f'Failed nonmatch: {m}')