"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
"""
with open('dataset_24465_4.txt') as one, open('dataset_24465_4_new.txt', 'w') as two:
    one_lines = one.read().splitlines()
    two_lines = one_lines[::-1]
    content = "\n".join(two_lines)
    two.write(content)