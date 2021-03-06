# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def conformity(group_a, group_b):
    for sample_a in group_a:         # В разборе здесь уже индекс, изящнее, но сама не додумалась
        index = group_a.index(sample_a)
        if index < len(group_b):
            yield sample_a, group_b[index]
        else:
            yield sample_a, None


example = conformity(tutors, klasses)

print(type(example))
print(*example)
