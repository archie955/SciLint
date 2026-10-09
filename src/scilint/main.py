import ast
from pathlib import Path


class Unit:
    def __init__(
        self,
        L: float = 0.0,
        M: float = 0.0,
        T: float = 0.0,
        A: float = 0.0,
        K: float = 0.0,
        mol: float = 0.0,
        cd: float = 0.0,
    ):
        self.L = L
        self.M = M
        self.T = T
        self.A = A
        self.K = K
        self.mol = mol
        self.cd = cd

    def __add__(self, other):
        return Unit(
            L=self.L + other.L,
            M=self.M + other.M,
            T=self.T + other.T,
            A=self.A + other.A,
            K=self.K + other.K,
            mol=self.mol + other.mol,
            cd=self.cd + other.cd,
        )

    def __radd__(self, other):
        return self + other

    def __mul__(self, other: float):
        return Unit(
            L=self.L * other,
            M=self.M * other,
            T=self.T * other,
            A=self.A * other,
            K=self.K * other,
            mol=self.mol * other,
            cd=self.cd * other,
        )

    def __rmul__(self, other: float):
        return self * other

    def __neg__(self):
        return Unit(
            L=self.L * -1,
            M=self.M * -1,
            T=self.T * -1,
            A=self.A * -1,
            K=self.K * -1,
            mol=self.mol * -1,
            cd=self.cd * -1,
        )

    def __sub__(self, other):
        return self + (-other)


class PhysCheck(ast.NodeVisitor):
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.errors = []
        self.persistent_errors = {}
        self.error_count = 0
