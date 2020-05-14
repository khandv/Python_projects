"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
Sample Input:

\w denotes word character
No slashes here
Sample Output:

\w denotes word character
"""
import sys
import re

for line in sys.stdin:
    if re.search(r"\\", line.strip()): print(line)
