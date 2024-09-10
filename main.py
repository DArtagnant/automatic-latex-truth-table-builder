import parse_logic as logic
import infers_cases as cases
import create_latex as latex


a = logic.Variable("A")
b = logic.Variable("B")
c = logic.Variable("C")

sentence = a | (b | a)

variables = [a, b]
table = cases.Table(logic.L3, variables)
cases_headers = cases.get_headers(sentence)
for case in cases_headers:
    table.insert_case(case)
print([[repr(e) for e in line] for line in table._table])

print(latex.create_latex(table._table,
                         ['$' + e.str_latex() + '$' for e in table._header]))