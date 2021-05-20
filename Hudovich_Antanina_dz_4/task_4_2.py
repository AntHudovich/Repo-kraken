import requests
import re
from datetime import date
# Написать функцию currency_rates(),
# принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.


def currency_rates(char_code='USD'):
    """
    get a currency rate
    :param char_code: international alphabetic currency code, ='USD'
    :return: currency rate
    """
    answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    reduced_answer = answer[answer.index('>') + 1:]
    char_code = char_code.upper()

    if char_code not in reduced_answer:
        return print(None)

    date_x, *moneys = re.split('<Valute', reduced_answer)
    # date_for_print = date[date.index('"') + 1:date.index('"') + 11]
    rate_date = date.today()

    for money in moneys:
        if char_code in money:
            nominal_start = money.find('<Nominal>')
            nominal_finish = money.find('</Nominal>')
            nominal = money[nominal_start + 9:nominal_finish]

            value_start = money.find('<Value>')
            value_finish = money.find('</Value>')
            value = float(money[value_start + 7:value_finish].replace(',', '.'))
            return print(f'По состоянию на {rate_date} {nominal} {char_code} = {value} RUR')


currency_rates('amd')
currency_rates('usd')
currency_rates('byn')
currency_rates('ftg')

# Очень тяжело далось задание. Если можно прошу скинуть твой пример выполнения д/з,
# т.к. по видео не видны некоторые строки и не удобно мотать вперед-назад.
# И еще может есть идея почему пустой return ни в какую не выводил None? с find() == -1 тоже.
