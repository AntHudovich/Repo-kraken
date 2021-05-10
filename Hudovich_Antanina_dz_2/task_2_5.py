# 5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться
# в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены
# получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров
# по возрастанию, написав минимум кода?

price_list = [12, 77.17, 23.9, 57, 82, 19.3, 25, 22.14, 65, 412, 1.9, 34.48]
print(id(price_list))
price_list.sort()
print(price_list, id(price_list))

for price in price_list:
    price_list[price_list.index(price)] = float(price)  # price_list[price_list.index(price)] = price * 1.00

string_of_prises = []
for float_price in price_list:
    float_price = str(float_price)
    ruble, penny = float_price.split('.')
    penny = int(penny)
    string_of_prises.append(f'{ruble} руб {penny:02d} коп')
print(string_of_prises)

print('цены, отсортированные по возрастанию: ', ', '.join(string_of_prises))
string_of_prises.reverse()
print('цены, отсортированные по убыванию: ', ', '.join(string_of_prises))
print('5 самых дорогих: ', ', '.join(string_of_prises[:5]))
print('5 самых дорогих по возрастанию: ', ', '.join(string_of_prises[4::-1]))
