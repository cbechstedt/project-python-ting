from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    word_search_list = []

    for index in range(len(instance)):
        file = instance.search(index)
        file_name = file["nome_do_arquivo"]
        file_lines = file["linhas_do_arquivo"]

        occurrence_list = []

        for line_index, line in enumerate(file_lines, start=1):
            if word.lower() in line.lower():
                occurrence_list.append({"linha": line_index})

        if occurrence_list:
            word_search_list.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrence_list,
                }
            )

    return word_search_list


def search_by_word(word, instance):
    ...
