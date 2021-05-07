# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

# Вариант 1, до 20
for quantity in range(21):
    if quantity == 1:
        print('1 процент')
    elif 2 <= quantity <= 4:
        print(quantity, 'процента')
    else:
        print(quantity, 'процентов')

# Вариант 2, для любого количества целых процентов
any_percent_else = int(input("Введи %: "))
if any_percent_else % 100 != 11 and any_percent_else % 10 == 1:
    print(any_percent_else, 'процент')
elif any_percent_else % 100 > 14 and 2 <= any_percent_else % 10 <= 4:
    print(any_percent_else, 'процента')
else:
    print(any_percent_else, 'процентов')
