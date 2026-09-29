import data
# Function to find the Most Expensive Book
def show_costliest_book():
    if len(data.book_prices) == 0:
        print("Library is empty!")
        return

    max_price = data.book_prices[0]
    max_name = data.book_names[0]

    for i in range(len(data.book_prices)):
        if data.book_prices[i] > max_price:
            max_price = data.book_prices[i]
            max_name = data.book_names[i]

    print("Most Expensive Book:", max_name)
    print("Price:", max_price)


# Function to display books in Reverse Order
def show_reversed_books():
    print("BOOKS IN REVERSE ORDER:")
    index = len(data.book_names) - 1
    while index >= 0:
        print("Name:", data.book_names[index])
        index = index - 1

