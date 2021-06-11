import re

# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.


class Close:
    def __init__(self, name):
        self.name = name

    @property
    def tissue_consumption(self):
        return 'consumption'

    def __add__(self, other):
        num_for_sum = re.compile(r'\d+\.\d+')

        result = float(num_for_sum.findall(self.tissue_consumption)[0]) + \
            float(num_for_sum.findall(other.tissue_consumption)[0])
        return f'All we need is {round(result, 2)} m^2'


class Coat(Close):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def tissue_consumption(self):
        consumption = round((self.size / 6.5 + 0.5), 2)
        return f'We need {consumption} m^2 of tissue to sew "{self.name}"'


class Suit(Close):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def tissue_consumption(self):
        consumption = 2 * self.height + 0.3
        return f'We need {consumption} m^2 of tissue to sew "{self.name}"'


if __name__ == '__main__':
    ghost = Coat('grey_man', 42)
    print(ghost.tissue_consumption)

    plankton = Suit('mr_scoliosis', 60)
    print(plankton.tissue_consumption)

    print(ghost + plankton)
# Гораздо проще было выводить обычные цифры в площадь, но решила потренироваться в регулярках заодно.
# Только не нашла, можно ли получить просто строку используя их? :(
