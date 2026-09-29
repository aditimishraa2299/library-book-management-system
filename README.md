# Library Book Management System

## Overview of the Project
The Library Book Management System is a modular Python-based Command Line Interface (CLI) application developed for the CSE1021 course. It automates essential library inventory operations, including inventory tracking, book issuance state management, dynamic pricing analytics, and reverse inventory traversal using structured parallel arrays.

## Features
- **View All Books:** Tabular display of inventory detailing Book ID, Title, Price, and real-time Availability status.
- **Add New Book:** Dynamic runtime entry appending new records to inventory lists.
- **Issue Book:** Instant toggle mechanism updating book availability status (`True` to `False` or vice-versa).
- **Find Most Expensive Book:** Automated linear search algorithm identifying the highest-priced book entity.
- **Reverse Display:** Algorithmic backward traversal displaying book details in reverse index order.
- **Interactive CLI Menu:** User-friendly menu loop with structured options and exit handling.

## Technologies/Tools Used
- **Programming Language:** Python 3.x
- **Development Environment:** Visual Studio Code / Terminal
- **Data Structures:** In-memory parallel lists/arrays
- **Version Control:** Git & GitHub

## Steps to Install & Run the Project

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/library-book-management.git](https://github.com/your-username/library-book-management.git)
   cd library-book-management

2. Verify File Structure:
Ensure the following module files are present in the directory:
​main.py
​data.py
​view_books.py
​issue.py
​analytics.py

Execute the Application:
Run the main menu script using Python 3:
python main.py


Instructions for Testing
​Unit Testing: Individual function execution testing in analytics.py and view_books.py.
​Integration Testing: Run main.py and trigger Menu Options 1 through 6 sequentially to test cross-module data flow with data.py.
​Boundary Testing: Input non-existent Book IDs during issuance or search operations to verify error handling.