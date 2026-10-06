"""
Examples of violations and non-violations for the first draft
"""
from typing import Literal
from typing import Annotated
UNITS: Literal["L", "M", "T", "A", "K", "mol", "cd"]

class Unit:
    def __init__(self, L: float = 0.0, M: float = 0.0, T: float = 0.0, A: float = 0.0, K: float = 0.0, mol: float = 0.0, cd: float = 0.0):
        self.L = L
        self.M = M
        self.T = T
        self.A = A
        self.K = K
        self.mol = mol
        self.cd = cd
        self.units: set[str] = {"L", "M", "T", "A", "K", "mol", "cd"}
        self.utou: dict[tuple[str, str], function] = {}

    def __add__(self, other):
        return Unit(
            L = self.L + other.L,
            M = self.M + other.M,
            T = self.T + other.T,
            A = self.A + other.A,
            K = self.K + other.K,
            mol = self.mol + other.mol,
            cd = self.cd + other.cd,
        )

    def __radd__(self, other):
        return self + other

    def __mul__(self, other: float | int):
        return Unit(
            L = self.L * other,
            M = self.M * other,
            T = self.T * other,
            A = self.A * other,
            K = self.K * other,
            mol = self.mol * other,
            cd = self.cd * other,
        )
    def __rmul__(self, other: float | int):
        return self * other

    def __neg__(self):
        return Unit(
            L = self.L * -1,
            M = self.M * -1,
            T = self.T * -1,
            A = self.A * -1,
            K = self.K * -1,
            mol = self.mol * -1,
            cd = self.cd * -1,
        )

    def __sub__(self, other):
        return self + (-other)

    def create_unit(self, unit: str):
        self.units.add(unit)

    def create_scaled_unit(self, unit: str, new_name: str, scale: float):
        if unit not in self.units:
            raise Exception

        

FACTOR = 0.5

Mass: Annotated[float, "sl:M"]
Velocity: Annotated[float, "sl:L/T"]
Energy: Annotated[float, "sl:E"]

def kinetic_energy(m: Mass, v: Velocity):
    return 0.5 * m * v**2