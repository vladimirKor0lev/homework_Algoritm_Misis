# Написать программу, которая фильтрует CSV файл с данными о продажах, оставляя только записи с суммой больше 1000 рублей.

import csv

with open("goods.csv", "r") as file:
    goods = list(csv.DictReader(file))

filtered_goods = []

for good in goods:
    if int(good["Сумма"]) > 1000:
        filtered_goods.append(good)

print(filtered_goods)
