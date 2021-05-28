import sys
from time import perf_counter
# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Придумала вот так
start = perf_counter()
unique_numbers = [number for number in src if src.count(number) == 1]
print(unique_numbers, perf_counter() - start)  # [23, 1, 3, 10, 4, 11] 1.730000000001175e-05
print(sys.getsizeof(unique_numbers))           # 120

# Сравнила с разбором домашки
start = perf_counter()
seen = set()
without_repetition = []
for number in src:
    if (number in seen) and (number in without_repetition):
        without_repetition.remove(number)
    else:
        without_repetition.append(number)
    seen.add(number)
print(without_repetition, perf_counter() - start)   # [23, 1, 3, 10, 4, 11] 2.6300000000006873e-05
print(sys.getsizeof(without_repetition))            # 120
# Какие минусы моего способа? Допустим ли?
