import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY, title TEXT, author TEXT)''')
    conn.commit()
    conn.close()

# Function to add a book to the database
def add_book(title, author):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''INSERT INTO books (title, author) VALUES (?, ?)''', (title, author))
    conn.commit()
    conn.close()

# Function to remove a book from the database
def remove_book(book_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
    conn.commit()
    conn.close()

# Function to retrieve all books from the database
def get_all_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM books''')
    books = c.fetchall()
    conn.close()
    return books

# Function to search for books by title or author
def search_books(keyword):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM books WHERE title LIKE ? OR author LIKE ?''', ('%'+keyword+'%', '%'+keyword+'%'))
    books = c.fetchall()
    conn.close()
    return books

# Main function to run the program
def main():
    initialize_database()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Search Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            add_book(title, author)
            print("Book added successfully!")
        elif choice == '2':
            book_id = input("Enter the ID of the book to remove: ")
            remove_book(book_id)
            print("Book removed successfully!")
        elif choice == '3':
            books = get_all_books()
            if not books:
                print("No books in the library.")
            else:
                print("Books in the library:")
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
        elif choice == '4':
            keyword = input("Enter the title or author keyword to search: ")
            found_books = search_books(keyword)
            if not found_books:
                print("No matching books found.")
            else:
                print("Matching books:")
                for book in found_books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

