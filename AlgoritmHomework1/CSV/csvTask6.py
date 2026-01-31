from lorem_text import lorem
from random import randint
import csv


with open('cities.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Город', 'Население'])

    for _ in range(1_000_001):
        writer.writerow([lorem.words(randint(1, 3)).title(), randint(10000, 100_000_000)])



