from connect import connect_database
conn = connect_database

def add_new_author(cursor, name, bio):
    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    values = (name, bio)
    cursor.execute(query, values)
    print("The author has been added. ")


def view_author_details(cursor, keyword):
    query = "SELECT id, name, bio FROM authors WHERE name LIKE %s"
    cursor.execute(query('%' + keyword + '%'))
    for author in cursor.fetchall():
        print(author)

def view_all_authors(cursor):
    query = "SELECT * FROM authors"
    cursor.execute(query)
    print(query)

def main():
    conn, cursor = connect_database()

    if conn is not None:
        try:
            print("1. add a new author \n2. search for an author \n3. display all authors")
            choice = input("Choose a number from the list above: ")

            if choice == "1":
                name = input("Enter the authorss name: ")
                bio = input("Enter a short bio about the author: ")
                add_new_author(cursor, name, bio)

            elif choice == "2":
                keyword = input("Enter the name you want to search for: ")
                view_author_details(cursor, keyword)
            else:
                view_all_authors(cursor)
        
        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
