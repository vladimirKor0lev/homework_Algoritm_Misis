# Реализуйте сжатие JSON-данных перед сохранением в файл и их распаковку при чтении.
import json
import gzip

data = {
    "name":"vladimir",
    "ip adress" : "102.064.55.4"
}

with gzip.open("data.json.gz", "wt", encoding="utf-8") as f:
    json.dump(data, f)
with gzip.open("data.json.gz", "rt", encoding="utf-8") as a:
    received_Data = json.load(a)
    print(received_Data)