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

    # TODO:
    # PK's are noted as: "*<column_name>",
    # and FK's are noted as: "+<column_name>"
    def to_json(self):
        return {
            self.name: self.type
        }
