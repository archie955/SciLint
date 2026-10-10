"""singleton for source of truth of all units"""

from dimensions import Dimension


class Units:
    instance = None
    __dims__: dict[str, Dimension] = {}
    __units__: set[str] = set()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    def add_dimension(cls, dim: Dimension):
        already_exists = cls.__dims__.get(dim.name)
        if already_exists:
            raise KeyError("dimensions name already taken")
        cls.__dims__[dim.name] = dim

    @classmethod
    def add_unit(cls, unit_name: str):
        if unit_name in cls.__units__:
            raise KeyError("unit already exists")
        cls.__units__.add(unit_name)
