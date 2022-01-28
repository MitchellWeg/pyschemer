class Database:
    conn = None
    cursor = None
    tables = None
    table_names = []

    def __init__(self, conn):
        self.cursor = conn.cursor()

    def draw(self):
        self.get_tables()
        self.describe_tables()

    def get_tables(self) -> [str]:
        self.cursor.execute("SHOW TABLES;")
        self.table_names = [t[0] for t in self.cursor.fetchall()]

        return self.tables

    def describe_tables(self):
        all_tables = []

        for table in self.table_names:
            _columns = []
            self.cursor.execute(f"DESCRIBE {table}")
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
                _columns.append(column)

            _table = Table(table, _columns)
            all_tables.append(_table)

        self.tables = all_tables

            
class Table:
    name = ""
    columns = []

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def __repr__(self) -> str:
        s = ""
        return s.join(f"{self.name}:\n {repr(self.columns)}\n")

class Column:
    name = ""
    type = ""
    null = False
    key_type = ""
    default = ""
    extra = ""

    def __init__(self, name: str, type: str, null: bool, key_type: str,
                 default: str, extra: str):
        self.name = name
        self.type = type
        self.null = null
        self.key_type = key_type
        self.default = default
        self.extra = extra

    def __repr__(self) -> str:
        return f"{self.name} {self.type} {self.null} {self.key_type} {self.default} {self.extra}"