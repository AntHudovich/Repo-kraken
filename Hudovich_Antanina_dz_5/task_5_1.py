# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
def odd_numbers(n):
    """get odd numbers from 1 to n"""
    for odd_number in range(1, n + 1, 2):
        yield odd_number


next_number = odd_numbers(7)
# print(*next_number)  if we want to see all the numbers
print(next(next_number))
print(next(next_number))

# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.


def odd_numbers_without_yield(n):
    """get odd numbers from 1 to n without yield use"""
    the_odd_number = (number for number in range(1, n + 1, 2))
    return the_odd_number


a = odd_numbers_without_yield(7)
print(next(a))
print(next(a))
print(next(a))
