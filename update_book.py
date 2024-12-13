from save_all_book import save_all_books

def update_book(all_books):
    
    search_book = input("Enter book title to update: ")
    
    flag = 0
    
    for book in all_books:        
        if book['title'] == search_book:
            
            flag+=1
            
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

    if flag == 0:    
        print("Sorry! Book not found.")
            