import data
# Function to add New Books
def add_book(b_id, name, price):
    if b_id in data.book_ids:
        print("This book ID already exists!")
    else:
        data.book_ids.append(b_id)
        data.book_names.append(name)
        data.book_prices.append(price)
        data.is_available.append(True)
        print("The New Book is added!")

# Function to issue a Book if available
def book_issue(b_id):
    if b_id in data.book_ids:
        idx = data.book_ids.index(b_id)
        if data.is_available[idx] == True:
            data.is_available[idx] = False
            print("The Book is issued successfully!")
        else:
            print("This Book is already issued!")
    else:
        print("Invalid Book ID!")
