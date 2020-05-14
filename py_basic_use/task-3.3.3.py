"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:

zabcz
zzxzz
"""
import sys
import re

pattern = re.compile(r"z.{3}z")
for line in sys.stdin:
    line = line.rstrip()
    if pattern.search(line): print(line)