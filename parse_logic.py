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
    
    def str_latex(self):
        return self._name
    
    def evaluate(self, variables_values):
        return variables_values[self]
        # for key, value in variables_values.items():
        #     if self._name == key._name:
        #         return value


class Op(OpBase): pass

class Not(Op):
    def __init__(self, a) -> None:
        self.a = a

    def __repr__(self) -> str:
        return f"(¬{self.a})"
    
    def evaluate(self, variables_values):
        inside = self.a.evaluate(variables_values)
        if inside is Logic_True():
            return Logic_False()
        elif inside is Logic_False():
            return Logic_True()
        else:
            return Logic_Unknown()
    
    def str_latex(self):
        return r"(\lnot " + self.a.str_latex() + ")"

class DoubleOp(Op):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

class Or(DoubleOp):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def __repr__(self) -> str:
        return f"({self.a} ∨ {self.b})"
    
    def str_latex(self):
        return "(" + self.a.str_latex() + r" \vee " + self.b.str_latex() + ")"
    
    def evaluate(self, variables_values):
        inside_a = self.a.evaluate(variables_values)
        inside_b = self.b.evaluate(variables_values)
        match inside_a, inside_b:
            case Logic_True(), Logic_True(): return Logic_True()
            case Logic_True(), Logic_False(): return Logic_True()
            case Logic_True(), Logic_Unknown(): return Logic_True()
            case Logic_False(), Logic_True(): return Logic_True()
            case Logic_False(), Logic_False(): return Logic_False()
            case Logic_False(), Logic_Unknown(): return Logic_Unknown()
            case Logic_Unknown(), Logic_True(): return Logic_True()
            case Logic_Unknown(), Logic_False(): return Logic_Unknown()
            case Logic_Unknown(), Logic_Unknown(): return Logic_Unknown()

class And(DoubleOp):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def __repr__(self) -> str:
        return f"({self.a} ∧ {self.b})"
    
    def str_latex(self):
        return "(" + self.a.str_latex() + r" \wedge " + self.b.str_latex() + ")"

class Logic_Value: pass

class Logic_True(Logic_Value):
    _elem = None
    def __new__(cls) -> Self:
        if cls._elem is not None:
            return cls._elem
        cls._elem = super().__new__(cls)
        return cls._elem
    
    def __repr__(self) -> str:
        return "V"

class Logic_False(Logic_Value):
    _elem = None
    def __new__(cls) -> Self:
        if cls._elem is not None:
            return cls._elem
        cls._elem = super().__new__(cls)
        return cls._elem

    def __repr__(self) -> str:
        return "F"
    

class Logic_Unknown(Logic_Value):
    _elem = None
    def __new__(cls) -> Self:
        if cls._elem is not None:
            return cls._elem
        cls._elem = super().__new__(cls)
        return cls._elem

    def __repr__(self) -> str:
        return "I"

L2 = {Logic_True(), Logic_False()}
L3 = {Logic_True(), Logic_False(), Logic_Unknown()}

if __name__ == "__main__":
    a = Variable("A")
    b = Variable("B")
    c = Variable("C")

    print(~a & b & (c | a))