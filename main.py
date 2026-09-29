import view_books
import book_ops
import analytics

# Main Program Menu Loop
while True:
    print("1. View All Books")
    print("2. Add New Book")
    print("3. Issue Book")
    print("4. Find Most Expensive Book")
    print("5. Show Books in Reverse Order")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        view_books.view_books()

    elif choice == "2":
        b_id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        price = float(input("Enter Price: "))
        book_ops.add_book(b_id, name, price)

    elif choice == "3":
        b_id = int(input("Enter Book ID to issue: "))
        book_ops.book_issue(b_id)

    elif choice == "4":
        analytics.show_costliest_book()

    elif choice == "5":
        analytics.show_reversed_books()

    elif choice == "6":
        print("Program Terminated.")
        break

    else:
        print("Invalid option chosen!")