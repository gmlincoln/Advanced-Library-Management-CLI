from save_all_book import save_all_books

def delete_book(all_books):
    search_book = input("Enter book title to delete: ")
    flag = 0     
    
    for book in all_books:
        
        if book['title'] == search_book:
            flag+=1
            all_books.remove(book)
            save_all_books(all_books)
            print("Book delete successfully!\n")
            return all_books    

    if flag == 0:    
        print("Sorry! Book not found.\n")