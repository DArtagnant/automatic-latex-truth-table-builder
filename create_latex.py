from tabulate import tabulate


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
    

def create_latex(data, headers) -> str:
    headers_c = ['$' + _remove_parenthesis(e.str_latex()) + '$' for e in headers]
    return _add_vertical_lines(
        len(headers_c),
        _build_latex(data, headers_c))


if __name__ == "__main__":
    data = [
    ["Alice", 24, "Ingénieure"],
    ["Bob", 27, "Designer"],
    ["Charlie", 22, "Développeur"]
    ]

    headers = ["Nom", "Âge", "Profession"]

    print(create_latex(data, headers))