class Table:
    name = ""
    columns = []

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def __repr__(self) -> str:
        s = ""
        return s.join(f"{self.name}:\n {repr(self.columns)}\n")