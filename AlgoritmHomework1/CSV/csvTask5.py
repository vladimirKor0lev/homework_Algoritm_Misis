# Написать программу, которая объединяет несколько CSV файлов с одинаковыми заголовками в один файл.
import csv

files = ['file1.csv', 'file2.csv']
all_data = []

with open('file1.csv', encoding='utf-8') as f:
    data = csv.DictReader(f)
    all_data.extend(list(data))

with open('file2.csv', encoding='utf-8') as f:
    data = csv.DictReader(f)
    all_data.extend(list(data))

with open('file3.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, all_data[0].keys())
    writer.writeheader()
    writer.writerows(sorted(all_data, key=lambda x:x['ID']))



