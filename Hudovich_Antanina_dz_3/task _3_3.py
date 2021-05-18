# 3. Написать функцию thesaurus(),
# принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы. Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Сможете ли вы вернуть отсортированный по ключам словарь?


def thesaurus(*names):
    names_list = [*names]
    dict_pair = {}
    while len(names_list) > 0:
        leader_name = names_list.pop()
        same_start = list(filter(lambda word: word.startswith(leader_name[0]), names_list))
        for name in same_start:
            if name.startswith(leader_name[0]):
                names_list.remove(name)
        same_start.append(leader_name)
        dict_pair[leader_name[0]] = same_start

    return print(dict_pair)


thesaurus('Ваня', 'Маня', 'Саня', 'Миша', 'Витя', 'Вадим', 'Влад')
