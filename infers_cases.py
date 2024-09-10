import parse_logic as logic


class Table:
    def __init__(self) -> None:
        self._table = []

    def insert_case(sentence):
        ...


def get_headers(assertion):
    if isinstance(assertion, logic.Variable):
        return []
    liste = get_headers(assertion.a)
    if isinstance(assertion, logic.DoubleOp):
        liste.extend(get_headers(assertion.b))
    liste.append(repr(assertion))
    return liste



if __name__ == "__main__":
    a = logic.Variable("A")
    b = logic.Variable("B")
    c = logic.Variable("C")

    sentence = (~a & b & (c | a))
    print("----------")
    print(sentence)
    print("----------")
    print(get_headers(sentence))