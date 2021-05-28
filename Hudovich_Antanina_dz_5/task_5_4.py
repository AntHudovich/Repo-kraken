import sys
# 4. Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

results = [number for number in src[1:] if number > src[src.index(number) - 1]]
res = (src[index] for index in range(1, len(src)) if src[index] > src[index - 1])

print(results)
print(*res)
print(sys.getsizeof(results))   # 120
print(sys.getsizeof(res))       # 112
