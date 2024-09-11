import parse_logic as logic
import infers_cases as cases
import create_latex as latex


a = logic.Variable("A")
b = logic.Variable("B")

sentence = a >> b

variables = [a, b]
table = cases.Table(logic.L3, variables)
for case in cases.get_headers(sentence):
    table.insert_case(case)

#debug check
print([[repr(e) for e in line] for line in table._table])

latex_tab = latex.create_latex_from_table(table)
print(latex_tab)
latex.save(latex_tab)