from tabulate import tabulate
import os

LATEX_DOC_BEGIN = r"""\documentclass{article}
\usepackage{booktabs}  % Optional for more attractive tables

\begin{document}

\section{Table example}

Here is an example of an automatically generated table inserted in this \LaTeX\ document:
\\
\\
"""

LATEX_DOC_END = r"""
\end{document}
"""


def _build_latex(data, headers) -> str:
    return tabulate(data, headers, tablefmt="latex_raw", numalign="center", stralign="center")

def _add_vertical_lines(nbr:int, str:str) -> str:
    return str.replace(
        '{' + 'c'*nbr + '}',
        '{' + '|c'*nbr + '|}')

def _remove_parenthesis(str):
    if str[0] == '(' and str[-1] == ')':
        return str[1:-1]
    else:
        return str

def create_latex_from_table(table):
    return create_latex(table._table, table._header)

def create_latex(data, headers) -> str:
    headers_c = ['$' + _remove_parenthesis(e.str_latex()) + '$' for e in headers]
    return _add_vertical_lines(
        len(headers_c),
        _build_latex(data, headers_c))

def save(str, file="./latex_output/output.tex"):
    try: os.makedirs(os.path.dirname(file))
    except FileExistsError: pass
    with open(file, 'w') as file:
        file.write(LATEX_DOC_BEGIN)
        file.write(str)
        file.write(LATEX_DOC_END)

if __name__ == "__main__":
    data = [
    ["Alice", 24, "Ingénieure"],
    ["Bob", 27, "Designer"],
    ["Charlie", 22, "Développeur"]
    ]

    headers = ["Nom", "Âge", "Profession"]

    print(create_latex(data, headers))