#!/usr/bin/env python3

import unicodedata as ud

import arabic_reshaper
from arabic_reshaper import ArabicReshaper
from arabicscript import ArabStr
from bidi.algorithm import get_display

HELLO = "مرحبًا"
QUATAR = "دولة قطر"

# configuration = {
#     'delete_harakat': True,
#     'support_ligatures': False,
#     'language': 'ArabicV2',
#     'RIAL SIGN': False,
# }
# reshaper = ArabicReshaper(configuration=configuration)
# reshaped_text = arabic_reshaper.reshape(HELLO)
# print(reshaped_text)
# for c in reshaped_text:
#     print(f'{c} U+{ord(c):04X} {ud.name(c)}')
# s = ud.normalize('NFKD', reshaped_text)

print(QUATAR[::-1])
enc = QUATAR.encode("cp1256")
enc = enc[::-1]
print(enc)
for c in QUATAR:
    print(f'{c} U+{ord(c):04X} {ud.name(c)}')

print('-' * 10)

