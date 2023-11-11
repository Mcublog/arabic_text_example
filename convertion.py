#!/usr/bin/env python3

import unicodedata as ud

import arabic_reshaper
from arabic_reshaper import ArabicReshaper
from arabicscript import ArabStr
from bidi.algorithm import get_display

HELLO = "مرحبًا"
"ﺎﺒﺣﺮﻣ"

configuration = {
    'delete_harakat': True,
    'support_ligatures': False,
    'language': 'ArabicV2',
    'RIAL SIGN': False,
}
# reshaper = ArabicReshaper(configuration=configuration)
reshaped_text = arabic_reshaper.reshape(HELLO)
print(reshaped_text)
# for c in reshaped_text:
#     print(f'{c} U+{ord(c):04X} {ud.name(c)}')
s = ud.normalize('NFKD', reshaped_text)
enc = s.encode("cp1256")
print(s)
print(enc)
for c in s:
    print(f'{c} U+{ord(c):04X} {ud.name(c)}')

print('-' * 10)
# bidi_text = get_display(reshaped_text, "cp864")
# enc = bidi_text.encode("cp864", "ignore").decode("cp864")
# for c in enc:
#     print(f'{c} U+{ord(c):04X} {ud.name(c)}')
# print(enc)
