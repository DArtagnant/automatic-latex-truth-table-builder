import parse_logic as logic
from itertools import product

class Table:
    def __init__(self, logic_system, variables:list) -> None:
        self._logic_system = logic_system
        self._header = variables
        self._variables = variables
        self._table = []
        self._insert_variables()

    def _insert_variables(self):
        for possibilite in product(self._logic_system, repeat=len(self._variables)):
            self._table.append(list(possibilite))

    def insert_case(self, sentence):
        for line in self._table:
            variables_values = dict(zip(self._variables, line))
            line.append(sentence.evaluate(variables_values))


def get_headers(assertion):
    if isinstance(assertion, logic.Variable):
        return []
    liste = get_headers(assertion.a)
    if isinstance(assertion, logic.DoubleOp):
        liste.extend(get_headers(assertion.b))
    liste.append(repr(assertion))
    return liste



if __name__ == "__main__":
    """
    

    sentence = (~a & b & (c | a))
    print("----------")
    print(sentence)
    print("----------")
    print(get_headers(sentence))
    """

    a = logic.Variable("A")
    b = logic.Variable("B")
    c = logic.Variable("C")

    table = Table(logic.L3, [a, b])
    table.insert_case(a | b)
    print([[repr(e) for e in line] for line in table._table])