#!/usr/bin/env python3

import unicodedata as ud

HELLO = "مرحبًا"
QUATAR = "دولة قطر"

# s = ud.normalize('NFKD', reshaped_text)

print(QUATAR[::-1])
enc = QUATAR.encode("cp1256")
enc = enc[::-1]
print(enc)
for c in QUATAR:
    print(f'{c} U+{ord(c):04X} {ud.name(c)}')

print('-' * 10)
