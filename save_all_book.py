from json import *

def save_all_books(all_books):
    with open("all_book.json", "w") as jsonFile:
        dump(all_books, jsonFile, indent=4)