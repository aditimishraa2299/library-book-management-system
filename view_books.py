import data
# Function to view all books and check their availability 
def view_books():
    print("ALL BOOKS IN LIBRARY:")
    i = 0
    while i < len(data.book_ids):
        print("ID:", data.book_ids[i])
        print("Name:", data.book_names[i])
        print("Price:", data.book_prices[i])
        if data.is_available[i] == True:
            print("Status: Available")
        else:
            print("Status: Issued")
        print(" ")
        i = i + 1
