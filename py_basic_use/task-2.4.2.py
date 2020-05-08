"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя
бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
"""
import os
import os.path

files_list = []
for curent_dir, dirs, files in os.walk('main'):
    for file in files:
        if file[-3:] == '.py':
            files_list.append(curent_dir.strip())

sort_list = sorted(set(files_list))

with open('sample_ans.txt', 'w') as ans:
    content = "\n".join(sort_list)
    ans.write(content)

# print(files_list)
# print(sort_list)
