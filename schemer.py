from table import Table
from column import Column

class Database:
    conn = None
    cursor = None
    tables = None
    table_names = []

    def __init__(self, conn):
        self.cursor = conn.cursor()

    def draw(self):
        self.get_tables()
        self.parse_tables()
        self.describe_tables()

    def get_tables(self):
        self.cursor.execute("SHOW TABLES;")

    def parse_tables(self) -> [str]:
        self.table_names = [t[0] for t in self.cursor.fetchall()]

        return self.table_names

    def describe_tables(self):
        all_tables = []

        for table in self.table_names:
            self.cursor.execute(f"DESCRIBE {table}")
            _columns = self.parse_describe()

            _table = Table(table, _columns)
            all_tables.append(_table)

        self.tables = all_tables

    def parse_describe(self):
        columns = []
        columns_in_table = self.cursor.fetchall()
        for col in columns_in_table:
            column = Column(
                col[0],
                col[1],
                False if col[2] == 'NO' else True,
                col[3],
                col[4],
                col[5]
            )
            columns.append(column) 

        return columns