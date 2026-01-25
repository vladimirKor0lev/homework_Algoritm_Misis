# Чтение JSON-файла
# 2.Дан файл data.json со следующей структурой:

import_data = '{ "name": "Иван", "age": 20, "courses": ["Математика", "Физика"]}'

#Напишите программу, которая прочитает файл и выведет имя студента.
import json

data = json.loads(import_data)

print(data["name"])
# 3. Добавьте в JSON-объект новое поле email и обновите файл на диске.
data["email"]="ivan2005@yandex.ru"
with open('write.json', 'w') as file:
    json.dump(data, file, indent=4)
