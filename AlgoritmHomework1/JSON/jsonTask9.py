import json

schema ={
    "Title": str,
    "Author": str,
    "Year": int
}


imported_data = json.load(open("bookslist.json", "r"))


for key, t in schema.items():
    for book in imported_data:
        if key not in book:
            print(ValueError(f"{book}: Missing field: {key}"))
            break
        if not isinstance(book[key], t):
            print(TypeError(f"{book}: {key} must be {t.__name__}"))



