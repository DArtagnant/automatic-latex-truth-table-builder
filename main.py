import parse_logic as logic
import infers_cases as cases
import create_latex as latex

# Define the variables you need here
a = logic.Variable("A")
b = logic.Variable("B")

# Write here the assertion for which you want to generate a truth table
#   ¬ is ~ (not)
#   ∨ is | (or)
#   ∧ is & (and)
#   ⇒ is >> (implies)
assertion = a >> b

# List all the variables you use here
variables = [a, b]


table = cases.Table(
    logic.L3, # Select whether you want classical propositional logic (L2) or Lukasiewicz logic (L3)
    variables
)
for case in cases.get_headers(assertion):
    table.insert_case(case)

#debug check
print([[repr(e) for e in line] for line in table._table])

latex_tab = latex.create_latex_from_table(table)
print(latex_tab)
latex.save(latex_tab) # This will save the result in a .tex file located at ./latex_output/output.tex