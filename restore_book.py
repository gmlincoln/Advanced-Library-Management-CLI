from json import load

def restore_all_books(all_books):
    with open("all_book.json", "r") as jsonFile:
        all_books = load(jsonFile)
    return all_books