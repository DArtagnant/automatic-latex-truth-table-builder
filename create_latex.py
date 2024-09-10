from tabulate import tabulate


def _build_latex(data, headers) -> str:
    return tabulate(data, headers, tablefmt="latex_raw", numalign="center", stralign="center")

def _add_vertical_lines(nbr:int, str:str) -> str:
    return str.replace(
        '{' + 'c'*nbr + '}',
        '{' + '|c'*nbr + '|}')
    
def create_latex(data, headers) -> str:
    return _add_vertical_lines(
        len(headers),
        _build_latex(data, headers))


if __name__ == "__main__":
    data = [
    ["Alice", 24, "Ingénieure"],
    ["Bob", 27, "Designer"],
    ["Charlie", 22, "Développeur"]
    ]

    headers = ["Nom", "Âge", "Profession"]

    print(create_latex(data, headers))