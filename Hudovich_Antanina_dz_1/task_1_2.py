# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Внимание: использовать только арифметические операции!

list_of_modified_numbers = []
for idx in range(1000):
    if not idx % 2:
        list_of_modified_numbers.append((idx + 1) ** 3)

print("Список кубов чисел от 1 до 1000:", list_of_modified_numbers)

# сумма чисел делящихся на 7
sum_of_numbers_divisible_by_seven = 0
for number in list_of_modified_numbers:
    number_for_chek = number
    sum_of_figures_in_number = 0
    while number_for_chek > 0:
        sum_of_figures_in_number += number_for_chek % 10
        number_for_chek = number_for_chek // 10
    if sum_of_figures_in_number % 7 == 0:
        sum_of_numbers_divisible_by_seven += number

print("Список т.н. делимых на 7:", sum_of_numbers_divisible_by_seven)


# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
# Вариант 1
list_of_modified_numbers_plus17 = []
for idx in range(1000):
    if not idx % 2:
        list_of_modified_numbers_plus17.append(((idx + 1) ** 3) + 17)
print("Новый список кубов от 1 до 1000, увеличенных на 17:", list_of_modified_numbers_plus17)

# Вариант 2 без нового списка
for number in range(len(list_of_modified_numbers)):
    list_of_modified_numbers[number] += 17
print("Не новый список кубов от 1 до 1000, увеличенных на 17:", list_of_modified_numbers)

sum_of_numbers_divisible_by_seven = 0
for number in list_of_modified_numbers:
    number_for_chek = number
    sum_of_figures_in_number = 0
    while number_for_chek > 0:
        sum_of_figures_in_number += number_for_chek % 10
        number_for_chek = number_for_chek // 10
    if sum_of_figures_in_number % 7 == 0:
        sum_of_numbers_divisible_by_seven += number

print("Список т.н. +17 делимых на 7:", sum_of_numbers_divisible_by_seven)
