"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
import csv
from collections import Counter

crimes = []
with open('crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        crimes.append(row[5])

print(Counter(crimes).most_common()[0])