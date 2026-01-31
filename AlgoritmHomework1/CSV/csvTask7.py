import pandas
def get_top10_frequent_values(file_path, column_name):
    # Используем chunksize для обработки файла по частям, если он очень большой
    chunk_size = 100000
    counts = pandas.Series(dtype=int)

    # Читаем CSV по частям (chunks)
    for chunk in pandas.read_csv(file_path, chunksize=chunk_size, usecols=[column_name]):
        # Подсчитываем значения в текущем чанке и обновляем общие результаты
        chunk_counts = chunk[column_name].value_counts()
        counts = counts.add(chunk_counts, fill_value=0)

    # Сортируем результаты и возвращаем топ-10
    top10 = counts.sort_values(ascending=False).head(10)
    return top10
print(get_top10_frequent_values("cities.csv", "Население"))