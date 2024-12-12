from connect import connect_database

conn = connect_database

def add_book(cursor, title, author_id, isbn, publication_date):
    query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
    values = (title, author_id, isbn, publication_date)
    print(cursor)
    cursor.execute(query, values)

def borrow_book(cursor, user_id, book_id, borrow_date, return_date):
    query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query(user_id, book_id, borrow_date, return_date))

def return_book(cursor, user_id, book_id, borrow_date, return_date):
    query = "DELETE FROM borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query(user_id, book_id, borrow_date, return_date))

def search_for_book(cursor, keyword):
    query = "SELECT id, title, isbn, availabilty FROM books WHERE title LIKE %s"
    cursor.execute(query, ('%' + keyword + '%'))
    for book in cursor.fetchall():
        print(book)

def display_all_books():
    conn = connect_database()
    cursor = conn.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)

def main():
    conn, cursor = connect_database()
    if conn is not None:
        try:

            print("1. add a book \n2. borrow a book \n3. return a boook \n4. search for a book \n5. display books")
            choice = input("Choose a number from the list above: ")

            if choice == "1":
                title = input("Enter the book title: ")
                author_id = input("Enter the authors ID: ")
                isbn = input("Enter the isbn: ")
                publication_date = input("Enter the publication date: ")
                add_book(cursor, title, author_id, isbn, publication_date)
            elif choice == "2":
                user_id = input("Enter user ID: ")
                book_id = input("Enter the book ID: ")
                borrow_date = input("Enter the date: ")
                return_date = input("When should the book be returned: ")
                borrow_book(cursor, user_id, book_id, borrow_date, return_date)
            elif choice == "3":
                user_id = input("Enter user ID: ")
                book_id = input("Enter book ID: ")
                borrow_date = input("When was the book borrowed: ")
                return_date = input("Enter the date: ")
                return_book(cursor, user_id, book_id, borrow_date, return_date)
            elif choice == "4":
                keyword = input("Enter the name of the book to look for: ")
                search_for_book(cursor, keyword)
            else:
                display_all_books()

        except Exception as e:
            print(e)

        finally:
            conn.close()
            cursor.close()

if __name__ == "__main__":
    main()
