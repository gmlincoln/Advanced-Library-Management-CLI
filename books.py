from add_book import add_books

all_books = []

while True:
    print("Welcome to Advance Library Management")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove/Delete Book")
    print("5. Lend Book")
    
    choice = input("Select an option: ")
    
    if choice == "0":
        print("Thanks for using library management system!\n")
        break 
    elif choice == '1':
        all_books = add_books(all_books)
    elif choice == '2':
        print("View all books")
    elif choice == '3':
        print("Update Book")
    elif choice == '4':
        print("Delete Book")
    elif choice == '5':
        print("Lend Book")
    else:
        print("Invalid Choice! Choose a valid option. ")    