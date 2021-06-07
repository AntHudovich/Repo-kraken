import os
# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
folder_for_check = r'C:\Users\tosha\PycharmProjects\pythonProject\Hudovich_Antanina_dz_7'


def files_size_stats(folder):
    dict_by_size = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            size_level = 10 ** (len(str(size)) + 1)
            dict_by_size.setdefault(size_level, []).append(file)

    size_counter = {key: len(vol) for key, vol in dict_by_size.items()}   # {10000: 2, 100000: 4, 100: 17}

    # Не знаю, важно ли сортировать ключи по размеру.
    list_keys = list(size_counter.keys())
    list_keys.sort()
    size_counter_sorted = {}
    for i in list_keys:
        size_counter_sorted[i] = size_counter[i]

    return print(size_counter_sorted)   # {100: 17, 10000: 2, 100000: 4}


if __name__ == '__main__':
    files_size_stats(folder_for_check)
