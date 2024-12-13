from add_book import add_books
from view_all_book import view_books
from restore_book import restore_all_books

from save_all_book import save_all_books

all_books = []

def update_book(all_books):
    
    search_book = input("Enter book title to update: ")
    
    for book in all_books:        
        if book['title'] == search_book:
            title = input("Enter book title: ")
            author = input("Enter author name: ")     
            published_year = int(input("Enter published year: "))
            price = input("Enter book price: ")    
            quantity = input("Enter book quantity: ")
            
            book['title'] = title
            book['author'] = author
            book['year'] = published_year
            book['price'] = price
            book['quantity'] = quantity
            
            save_all_books(all_books)
            print("Book updated successfully!")
            return all_books    


while True:
    print("Welcome to Advance Library Management")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove/Delete Book")
    print("5. Lend Book")
    
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
        print("Delete Book")
        
    elif choice == '5':
        print("Lend Book")
        
    else:
        print("Invalid choice! Please try again.\n")    