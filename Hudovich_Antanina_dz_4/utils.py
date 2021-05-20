import requests
import re
from datetime import date


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

