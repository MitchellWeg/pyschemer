import pymonetdb

import pyschemer
from pyschemer.schemer import Database

class Monet(Database):
    schema = ""

    def get_dot(self, schema):
        self.schema = schema

        return super().get_dot()

    def get_tables(self, q=None):
        return super().get_tables(q="SELECT name FROM sys.tables WHERE system=false")

    def describe_tables(self):
        all_tables = {}

        for table in self.table_names:
            self.cursor.execute(f"SELECT name, type FROM describe_columns('{self.schema}', '{table}')")
            _table = self.cursor.fetchall()

            if len(_table) > 0:
                cols = {}
                for column in _table:
                    cols[column[0]] = column[1]

                all_tables[table] = cols


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

    db = Monet(conn=conn, db_name="foo")
    foo_dot = db.get_dot("foo")
    bar_dot = db.get_dot("bar")

    db.draw(foo_dot, "monet_out_foo")
    db.draw(bar_dot, "monet_out_bar")


if __name__ == '__main__':
    main()