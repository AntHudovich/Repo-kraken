# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        return f'Машина поехала'

    @staticmethod
    def stop():
        return f'Машина остановилась'

    @staticmethod
    def turn(direction):
        return f'Машина повернула на {direction}'

    def show_speed(self):
        return f'Скорость движения {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили допустимую скорость движения')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили допустимую скорость движения')


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    dzilli = WorkCar(12, 'grey', 'dzhili_byli', False)
    print(dzilli.name)
    dzilli.show_speed()

    moskvich = SportCar(90, 'scarlet', 'swallow', False)
    print(moskvich.color, moskvich.name)
    moskvich.show_speed()

    trolley = TownCar(61, 'blue', 'crowd', False)
    print(trolley.go())
    print(trolley.turn('лево'))
    trolley.show_speed()

    minibus = PoliceCar(120, 'nondescript', 'disgusting', True)
    print(minibus.is_police)
