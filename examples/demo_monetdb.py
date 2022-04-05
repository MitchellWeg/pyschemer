import sys
import pymonetdb

from pyschemer.schemer import Database

class Monet(Database):
    schema = ""
    schema_id = None

    def get_dot(self, schema):
        self.schema = schema if schema else 'sys'

        self.schema_id = self.get_schema_id(self.schema)

        return super().get_dot()

    def get_tables(self, q=None):
        q = f"""SELECT tables.name
                                FROM sys.tables
                                JOIN sys.schemas ON schemas.id = tables.schema_id
                                WHERE tables.system=false
                                and schemas.name='{self.schema}'"""

        return super().get_tables(q)

    def describe_tables(self):
        all_tables = {}

        for table in self.table_names:
            q = f"SELECT name, type FROM describe_columns('{self.schema}', '{table}')"
            self.cursor.execute(q)
            _table = self.cursor.fetchall()

            if len(_table) > 0:
                cols = {}
                for column in _table:
                    cols[column[0]] = column[1]

                all_tables[table] = cols

        self.tables = all_tables

    def get_relationships(self, q=None):
        q = f"""
        SELECT fk, fk_t, fk_c, pk_t, pk_c FROM describe_foreign_keys WHERE fk_s = '{self.schema}';
        """
        return super().get_relationships(q)

    def get_schema_id(self, schema):
        q = f"SELECT id FROM sys.schemas WHERE name = '{schema}'"
        rows = self.cursor.execute(q)

        if rows <= 0:
            print(f"Couldnt get ID for schema '{schema}'.")
            print(f"This schema most likely does not exist.")
            sys.exit(-1)

        id = self.cursor.fetchall()[0][0]

        return id

def main():
    conn = pymonetdb.connect(
        username='monetdb',
        password='monetdb',
        hostname='localhost',
        port=50000,
        database="demo"
    )

    db = Monet(conn=conn, db_name="foo")
    foo_dot = db.get_dot("sys")
    db.draw(foo_dot, "monet_out_foo")

    bar_dot = db.get_dot("bar")
    db.draw(bar_dot, "monet_out_bar")


if __name__ == '__main__':
    main()