#Создать программу, которая обрабатывает большой CSV файл (более 1 млн строк) и находит топ-10 самых частых значений в определенном столбце.

# Данные взять из предыдущего задания (6-е задание)
# import pandas
# def get_top10_frequent_values(file_path, column_name):
#     # Используем chunksize для обработки файла по частям, если он очень большой
#     chunk_size = 100000
#     counts = pandas.Series(dtype=int)
#
#     # Читаем CSV по частям (chunks)
#     for chunk in pandas.read_csv(file_path, chunksize=chunk_size, usecols=[column_name]):
#         # Подсчитываем значения в текущем чанке и обновляем общие результаты
#         chunk_counts = chunk[column_name].value_counts()
#         counts = counts.add(chunk_counts, fill_value=0)
#
#     # Сортируем результаты и возвращаем топ-10
#     top10 = counts.sort_values(ascending=False).head(10)
#     return top10
# print(get_top10_frequent_values("cities.csv", "Население"))

import pandas as pd
# import curl_cffi

df = pd.read_csv('cities.csv')

print(df['Город'].value_counts())
print(df['Население'].value_counts())

# r = curl_cffi.get('https://simple.wikipedia.org/wiki/Afghanistan', impersonate="chrome110")

# print(r.content)

# with open('test.html', 'w') as f:
#     f.write(r.text)


df = pd.read_html('test.html')

print(df[1]['Area (km²)'].median())

