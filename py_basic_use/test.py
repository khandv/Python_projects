import re

lst = [
    "+ blabla is a tandem repetition",  # ['bla'] <_sre.SRE_Match object; span=(2, 8), match='blabla'>
    "+ 123123 is good too",  # ['123'] <_sre.SRE_Match object; span=(2, 8), match='123123'>
    "- go go",   # [] None
    "+ 22",      # ['2'] <_sre.SRE_Match object; span=(2, 4), match='22'>
    "- 333",     # [] None
    "+ 4444",    # ['44'] <_sre.SRE_Match object; span=(2, 6), match='4444'>
    "- 55555",   # [] None
    "+ 666666",  # ['666'] <_sre.SRE_Match object; span=(2, 8), match='666666'>
]

pattern = r'(.)-\2'
for line in lst:
    print(re.findall(pattern, line), re.search(pattern, line))