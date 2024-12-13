from save_all_book import save_all_books

from datetime import datetime, timedelta
from json import *

def lend_book(all_books):
    search_book = input("Enter the title of the book you want to borrow: ")
    flag = 0
    for book in all_books:
        if book['title'] == search_book:
            flag+=1
            quantity = int(book['quantity'])
            
            if quantity > 0:  
                borrower_name = input("Enter borrower's name: ")
                phone_number = input("Enter borrower's phone number: ")
                
                # Generate a return due date (7 days from today)
                due_date = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
                
                # Save the lend information
                lend_info = {
                    "borrower_name": borrower_name,
                    "phone_number": phone_number,
                    "book_title": search_book,
                    "lend_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "due_date": due_date,
                }
                
                # Append lend information to a file
                try:
                    with open("lend_info.json", "a") as lend_file:
                        dump(lend_info, lend_file, indent=4)
                        
                except Exception as e:
                    print(f"Error saving lend information: {e}")
                
                
                
                # Decrease the quantity of the book
                book['quantity'] = quantity - 1
                
                # Save the updated books list
                save_all_books(all_books)
                
                print(f"Book '{search_book}' has been lent to {borrower_name}. Please return by {due_date}.")
            
            else:
                print("There are not enough books available to lend.\n")
    
    if flag == 0:    
        print("Sorry! Book not found.\n")
