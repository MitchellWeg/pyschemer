import mariadb
import sys
from schemer.schemer import Database

def main():
    try:
        conn = mariadb.connect(
            user="root",
            password="secret",
            host="127.0.0.1",
            port=3306,
            database="foo"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    db = Database(conn, "foo")
    db.draw('out_maria')

if __name__ == "__main__":
    main()