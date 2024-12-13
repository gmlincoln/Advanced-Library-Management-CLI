from save_all_book import save_all_books
from lend_book import lend_book
def return_book(all_books):
    search_book = input("Enter the title of the book you are returning: ")
    phone_number = input("Enter borrower's phone number: ")

    flag = 0
    
    for book in all_books:
        
        if book['title'] == search_book:
            
            flag+=1
            
            book['quantity'] = int(book['quantity'] + 1)
            
            save_all_books(all_books)            
            print(f"Book '{search_book}' has been returned successfully.")
    
            
    
    if flag == 0:
        print("Sorry! Book not found.")
