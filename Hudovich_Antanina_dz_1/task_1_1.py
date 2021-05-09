# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input("Введите длительность в секундах "))
minutes = duration // 60
# print('Соответственно округленно', minutes, 'минут')
seconds = duration % 60
# print('или', minutes, 'минут', 'и', seconds, 'секунд')
hours = minutes // 60
minutes_under_hours = duration // 60 % 60
# print('или', hours, 'часов', minutes_under_hours, 'минут', 'и', seconds, 'секунд')
days = hours // 24
# print('и наконец', days, 'дней', hours, 'часов', minutes_under_hours, 'минут', 'и', seconds, 'секунд')
if duration < 60:
    print(seconds, 'сек')
elif duration < 3600:
    print(minutes, 'мин', seconds, 'сек')
elif duration < 86400:
    print(hours, 'час', minutes_under_hours, 'мин', seconds, 'сек')
else:
    print(days, 'дн', hours, 'час', minutes_under_hours, 'мин', seconds, 'сек')
