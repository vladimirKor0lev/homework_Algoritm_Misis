#
# Вложенные структуры
#
# Создайте JSON-объект, представляющий каталог товаров с вложенной структурой (категория → подкатегория → товары). Реализуйте поиск товара по названию.
import json
import random
from string import ascii_letters
from xml.etree.ElementTree import indent

categories = ['Auto', 'PC', 'Food', 'Books']

subcategoris_auto = ['Moto', 'VAZ', "BMW"]
subcategoris_pc = ['RAM', 'CPU', "Motherboard"]
subcategoris_food = ['Fruits', 'Vegetables', "Meat"]
subcategoris_book = ['Science', 'IT', "Ezoterica"]

store = {}

for category in categories:
    store[category] = {}
    if category == 'Auto':
        for subcategory in subcategoris_auto:
            store[category][subcategory] = [''.join(random.sample(ascii_letters, 6)) for i in range(5)]
    elif category == 'PC':
        for subcategory in subcategoris_pc:
            store[category][subcategory] = [''.join(random.sample(ascii_letters, 6)) for i in range(5)]
    elif category == 'Food':
        for subcategory in subcategoris_food:
            store[category][subcategory] = [''.join(random.sample(ascii_letters, 6)) for i in range(5)]
    elif category == 'Books':
        for subcategory in subcategoris_book:
            store[category][subcategory] = [''.join(random.sample(ascii_letters, 6)) for i in range(5)]


json.dump(store, open('store.json', 'w'), indent=4)