
# Обработка ошибок

# Напишите программу, которая пытается прочитать JSON-файл и обрабатывает возможные ошибки (файл не найден, некорректный формат).

import json

filepath = input('Input filepath: ')

try:
    data = json.load(open(filepath, 'r'))
    print(data)
except FileNotFoundError as e:
    print('File not found', e)
except json.decoder.JSONDecodeError as e:
    print('Invalid file format', e)
