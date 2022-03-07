import pymonetdb
from schemer.schemer import Database

class Monet(Database):
    def get_tables(self, q=None):
        return super().get_tables(q="SELECT name FROM sys.tables WHERE system=false")

    def describe_tables(self):
        all_tables = []

        # TODO: the schema here needs to be fixed.
        for table in self.table_names:
            self.cursor.execute(f"SELECT name, type FROM describe_columns('sys', '{table}')")
            _table = self.cursor.fetchall()
            all_tables.append(_table)

        self.tables = all_tables

    def get_relationships(self, q=None):
        return []

def main():
    conn = pymonetdb.connect(
        username='monetdb',
        password='monetdb',
        hostname='localhost',
        port=50000,
        database="demo"
    )

    db = Monet(conn, "foo")
    db.draw()


if __name__ == '__main__':
    main()