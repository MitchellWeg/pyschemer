import prettytable


class Table:
    name = ""
    columns = []

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def to_json(self):
        out = {}

        for x in self.columns:
            out[x.name] = x.type

        return {
            f"{self.name}": out
        }

    def print(self):
        x = prettytable.PrettyTable(
            ["Field", "Type", "Null", "Key", "Default", "Extra"]
        )
        for i in self.columns:
            x.add_row([i.name, i.type, i.null, i.key_type, i.default, i.extra])

        print(x)
