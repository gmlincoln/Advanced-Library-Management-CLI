
def view_books(all_books):
    
    if all_books != []:
        for i, book in enumerate(all_books, start=1):
            print(f"\nBook Number: {i}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Published Year: {book['year']}")
            print(f"Quantity: {book['quantity']}")
            print(f"ISBN No: {book['isbn']}")
            print(f"Book Added At: {book['bookAddedAt']}\n")
    else:
        print("No book found in the library!")