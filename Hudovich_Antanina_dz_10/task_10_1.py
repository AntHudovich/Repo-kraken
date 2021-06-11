# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
class Matrix:
    def __init__(self, number_matrix):
        self.number_matrix = number_matrix

    def __str__(self):
        result = ''
        for raw in self.number_matrix:
            for num in raw:
                result += str(num)
                result += '\t'
            result += '\n'
        return result

    # def __add__(self, other):
    #     sum_result = ''
    #     for raw in range(len(self.number_matrix)):
    #         for num in range(len(self.number_matrix[raw])):
    #             sum_result += str(self.number_matrix[raw][num] + other.number_matrix[raw][num])
    #             sum_result += '\t'
    #         sum_result += '\n'
    #     return sum_result
    def __add__(self, other):
        sum_result = []
        for raw in range(len(self.number_matrix)):
            sum_raw = []
            for num in range(len(self.number_matrix[raw])):
                sum_raw.append(self.number_matrix[raw][num] + other.number_matrix[raw][num])
            sum_result.append(sum_raw)
        result = Matrix(sum_result)
        return result


list_list = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
beta_list = [[5, 7, 6], [8, 3, 4], [9, 0, 3], [4, 8, 2]]
a = Matrix(list_list)
b = Matrix(beta_list)
print(a)
print(a + b)
# Как лучше делать вывод "+": через образец матрицы или через строку для принта?
