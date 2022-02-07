class Relationship:
    constraint_name = ""
    table_name = ""
    column_name = ""
    referenced_table_name = ""
    referenced_column_name = ""

    def __init__(self, constraint_name, table_name, column_name, ref_table, ref_column):
        self.constraint_name = constraint_name
        self.table_name = table_name
        self.column_name = column_name
        self.referenced_table_name = ref_table
        self.referenced_column_name = ref_column

    def to_json(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.table_name}:{self.column_name} 1--1 {self.referenced_table_name}:{self.referenced_column_name}"


