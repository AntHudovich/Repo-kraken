from time import sleep
# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    def __init__(self):
        self.__color = 'off'

    def running(self):
        self.__color = 'red'
        yield self.__color
        sleep(7)
        self.__color = 'yellow'
        yield self.__color
        sleep(2)
        self.__color = 'green'
        yield self.__color
        sleep(10)


if __name__ == '__main__':
    my_street_star = TrafficLight()
    my_street_star.running()

    lights_order = []
    for light in my_street_star.running():
        lights_order.append(light)

    if lights_order == ['red', 'yellow', 'green']:
        print('It works!')
    else:
        print("It's broken again :(")
# Я думала, что нужно выводить смену режимов через принт, но тогда получается облом с проверкой работы.
