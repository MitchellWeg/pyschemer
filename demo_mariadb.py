import mariadb
import sys
from schemer import Database

def main():
    try:
        conn = mariadb.connect(
            user="foo",
            password="foo",
            host="localhost",
            port=3306,
            database="my-database"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    db = Database(conn)
    db.draw()
    print(db.tables)

if __name__ == "__main__":
    main()