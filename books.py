from add_book import add_books
from view_all_book import view_books
from restore_book import restore_all_books
from update_book import update_book
from delete_book import delete_book
from lend_book import lend_book
from return_book import return_book


all_books = []

while True:
    print("===Advance Library Management System===")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove/Delete Book")
    print("5. Lend Book")
    print("6. Return Book")
    
    all_books = restore_all_books(all_books)
    
    choice = input("Select an option: ")
    
    if choice == "0":
        print("Thanks for using library management system!\n")
        break 
    
    elif choice == '1':
        all_books = add_books(all_books)
        
    elif choice == '2':
        view_books(all_books)
        
    elif choice == '3':
        update_book(all_books)
        
    elif choice == '4':
        delete_book(all_books)
        
    elif choice == '5':
        lend_book(all_books)
        
    elif choice == '6':
        return_book(all_books)
        
    else:
        print("Invalid choice! Please try again.\n")    