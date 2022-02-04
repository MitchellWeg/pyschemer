import mariadb
import sys
from schemer.schemer import Database

def main():
    try:
        conn = mariadb.connect(
            user="mitchell",
            password="foo",
            host="localhost",
            port=3306,
            database="TinderForCats"
        )
    except mariadb.Error as e:
        # print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    db = Database(conn, "TinderForCats")
    db.draw()

if __name__ == "__main__":
    main()