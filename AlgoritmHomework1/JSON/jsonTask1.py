#  Создание JSON-объекта
# Создайте словарь с информацией о студенте (имя, возраст, оценки) и преобразуйте его в JSON-формат. Выведите результат в консоль.
import json

data = {
    "name": "Diana",
    "age": 24,
    "courses_and_scores": {"Literature":5, "Philosophy":4},
}
json_Data = json.dumps(data)
print(json_Data)