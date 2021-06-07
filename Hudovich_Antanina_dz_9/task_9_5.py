# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        return f'{self.title}: Положи немедленно! Это журнальная ручка!!!'


class Pencil(Stationary):
    def draw(self):
        return f'{self.title}: Где где... За ухом или в гульке'


class Handle(Stationary):
    def draw(self):
        return f'{self.title}: Жирный жирный жирный, как поезд пассажирный'


if __name__ == '__main__':
    parker = Pen('Mr. Parker')
    print(parker.draw())

    maped = Pencil('Mr. Maped')
    print(maped.draw())

    faber_castell = Handle('Mr. Faber-Castell')
    print(faber_castell.draw())

# Я не знаю, почему не работает простой ретурн, я не понимаю, он не печататет строку в вывод. Почемуууу???????
