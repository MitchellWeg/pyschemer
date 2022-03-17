from erdot.__main__ import splitJSONIntoChuncks, generateDotCode
import json
import pygraphviz as pgv
from .table import Table
from .column import Column
from .relationships import Relationship


class Database:
    database_name = ""
    conn = None
    cursor = None
    tables = None
    table_names = []
    relationships = []

    def __init__(self, conn, db_name):
        self.cursor = conn.cursor()
        self.database_name = db_name

    def get_dot(self):
        self.get_tables()
        self.get_table_names()
        self.describe_tables()
        self.get_relationships()

        dot_code = self.generate_dot_code(self.to_json())

        return dot_code
        
    def draw(self, dot_code, filename='out'):
        G = pgv.AGraph(string=dot_code)
        schema_drawing = G.draw(path=None, format='jpeg', prog='dot')

        with open(f'{filename}.jpg', 'wb') as outfile:
            outfile.write(schema_drawing)

    def generate_dot_code(self, db_json) -> str:
        json_loaded = json.loads(db_json)
        chunked_json = splitJSONIntoChuncks(json_loaded)
        string_gen = generateDotCode(chunked_json)
        return string_gen

    def get_tables(self, q="SHOW TABLES;"):
        self.cursor.execute(q)

    def get_table_names(self) -> [str]:
        self.table_names = [t[0] for t in self.cursor.fetchall()]

        return self.table_names

    def describe_tables(self):
        all_tables = {}

        for table in self.table_names:
            self.cursor.execute(f"DESCRIBE {table}")
            _table = self.cursor.fetchall()
            cols = {}
            for column in _table:
                cols[column[0]] = column[1]

            all_tables[table] = cols

        self.tables = all_tables

    def parse_tables(self):
        out = []
        for table in self.tables:
            _columns = self.parse_describe()
            _table = Table(table, _columns)
            out.append(_table.to_json())

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

    def get_relationships(self, q=None):
        if q is None:
            q = ("SELECT CONSTRAINT_NAME, TABLE_NAME,"
                 "COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME",
                 "FROM information_schema.KEY_COLUMN_USAGE",
                 "WHERE CONSTRAINT_SCHEMA = '{self.database_name}'",
                 "AND CONSTRAINT_NAME <> 'PRIMARY';"
                 )

        self.cursor.execute(q)

        self.relationships = self.parse_relationships()

    def parse_relationships(self) -> [Relationship]:
        out = []
        info_schema = self.cursor.fetchall()
        for col in info_schema:
            if all(col):
                out.append(Relationship(
                    col[0],
                    col[1],
                    col[2],
                    col[3],
                    col[4]
                ))

        return out

    def to_json(self) -> str:
        out = {}
        all_relationships = self.to_list(self.relationships)

        out = {
            "tables": self.tables,
            "relations": all_relationships,
            "rankAdjustments": "",
            "label": ""
        }

        return json.dumps(out)

    def to_list(self, input) -> []:
        return [x.to_json() for x in input]
