from types import UnionType
from typing import Any, Self

class OpBase:
    def __and__(self, other:Self):
        assert isinstance(other, OpBase)
        return And(self, other)
    
    def __or__(self, other: Self):
        assert isinstance(other, OpBase)
        return Or(self, other)
    
    def __invert__(self):
        return Not(self)

class Variable(OpBase):
    def __init__(self, name:str) -> None:
        self._name = name

    def __repr__(self) -> str:
        return self._name


class Op(OpBase): pass

class Not(Op):
    def __init__(self, a) -> None:
        self.a = a

    def __repr__(self) -> str:
        return f"(¬{self.a})"

class DoubleOp(Op):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

class Or(DoubleOp):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def __repr__(self) -> str:
        return f"({self.a} ∨ {self.b})"

class And(DoubleOp):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def __repr__(self) -> str:
        return f"({self.a} ∧ {self.b})"



if __name__ == "__main__":
    a = Variable("A")
    b = Variable("B")
    c = Variable("C")

    print(~a & b & (c | a))