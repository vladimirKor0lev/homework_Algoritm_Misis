#4. Работа с массивами
# Создайте JSON-файл, содержащий список словарей с информацией о книгах (название, автор, год издания). Добавьте функцию для поиска книг по автору.
import json

booklist = [
    {
        'Title': "The Prince",
        "Author": "Machivalli",
        "Year": 1600
    },
    {
        'Title': "The asdfasdfasdfasdf",
        "Author": "Machivalli",
        "Year": 1620
    },
    {
        "Title": 'Beastars',
        "Author": "Paru",
        "Year": 2010
    }
]

jsonBooklist = json.dump(booklist, fp=open('bookslist.json', 'w'), indent=4)

def search_book(filepath: str, author: str) -> list:
    json_book_list = json.load(open(filepath, 'r'))
    found_books = []

    for book in json_book_list:
        if book['Author'].lower() == author.lower():
            found_books.append(book)

    return found_books




print(search_book('bookslist.json', 'pArU'))


# s = 'helloworld'
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
#
# print(s.isalpha())
# print(s.isalnum())
# print(s.isdigit())
# print(s.isspace())






