import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "library_db"
    user = "root"
    password = "Luna2794"
    host = "localhost"

    try:
        conn = mysql.connector.connect(database = db_name, user = user, password = password, host = host)
        cursor = conn.cursor()
        if conn.is_connected():
            print("connected")
            return conn, cursor

    except Error as e:
        print(e)
        return None

if __name__ == "__connect_database__":
    connect_database()