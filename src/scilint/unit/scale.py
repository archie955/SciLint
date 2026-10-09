class Scale:
    def __init__(
        self, name: str, symbol: str, factor: float = 1.0, offset: float = 0.0
    ):
        self.name = name
        self.symbol = symbol
        self.factor = factor
        self.offset = offset

    def to_base(self, value: float) -> float:
        return value * self.factor + self.offset

    def from_base(self, value: float) -> float:
        return (value - self.offset) / self.factor

    def __repr__(self) -> str:
        return f"<Scale {self.name} ({self.symbol})"
