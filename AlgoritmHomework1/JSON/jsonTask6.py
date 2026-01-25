# Преобразование данных

# Преобразуйте JSON-объект, содержащий список температур за месяц, в словарь, где ключами будут даты, а значениями — температуры.

import json

weather = json.load(open('weather.json', 'r'))

weather_dict = {}

date = 21
for day in weather:
    weather_dict[f'{date}.01.2026'] = day
    date += 1

print(weather_dict)

