import sys


def test():
    array = [1, 2, 3, 4, 5]
    is_3_in_array = 3 in array
    print(is_3_in_array)


test()


def txt_importer(path_file):
    array = [1, 2, 3, 4, 5]
    is_3_in_array = 3 in array
    print(is_3_in_array)
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            lines_list = file.read().split("\n")
            return lines_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
