from random import *
from datetime import *

from save_all_book import save_all_books

def add_books(all_books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")     
    published_year = input("Enter published year: ")
    price = input("Enter book price: ")    
    quantity = input("Enter book quantity: ")  
    isbn =  randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    

    book = {
        "title": title,
        "author": author,
        "year": published_year,
        "price": price,
        "quantity": quantity,
        "isbn": isbn,
        "bookAddedAt": bookAddedAt,
    }
    
    all_books.append(book)
    save_all_books(all_books)
    print("Book added successfully!")