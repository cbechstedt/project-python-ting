from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file_lines = txt_importer(path_file)
    file_result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }
    instance.enqueue(file_result)
    print(file_result)


def remove(instance: Queue):
    if len(instance) == 0:
        return print("Não há elementos")
    popped_file = instance.dequeue()
    popped_file_path = popped_file["nome_do_arquivo"]
    print(f"Arquivo {popped_file_path} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
