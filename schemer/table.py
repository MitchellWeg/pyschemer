import prettytable

class Table:
    name = ""
    columns = []

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def print(self):
        x = prettytable.PrettyTable(["Field", "Type", "Null", "Key", "Default", "Extra"])
        for i in self.columns:
            x.add_row([i.name, i.type, i.null, i.key_type, i.default, i.extra])

        print(x)
