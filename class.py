class Schema:
    def __init__(self):
        self.version = None
        self.name = None
        self.description = None
        self.domains = list()
        self.tables = list()


class Table:
    def __init__(self):
        self.name = None
        self.add = False
        self.edit = False
        self.delete = False
        self.fields = list()
        self.constraints = list()
        self.indices = list()


class Field:
    def __init__(self):
        self.name = None
        self.rname = None
        self.position = None
        self.domain = None
        self.description = None
        self.show_in_grid = False
        self.show_in_details = False
        self.autocalculated = False
        self.required = False


class Domain:
    def __init__(self):
        self.name = None
        self.description = None
        self.type = None
        self.align = None
        self.width = None
        self.show_null = False
        self.show_lead_nulls = False
        self.thousands_separator = False
        self.length = None
        self.precision = None
        self.scale = None


class Constraint:
    def __init__(self):
        self.name = None
        self.kind = None
        self.items = None
        self.reference = None
        self.expression = None
        self.has_value_edit = False
        self.cascading_delete = False


class Index:
    def __init__(self):
        self.name = None
        self.field = None
        self.fulltext = False
        self.uniqueness = False
        self.local = False
