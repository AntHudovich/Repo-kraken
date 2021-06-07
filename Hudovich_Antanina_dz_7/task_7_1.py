import os
import sys
# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали


def main(argv):
    program, *args = argv
    grow_up_tree(*args)


def grow_up_tree(yaml_file):

    def up_by_tree(n):
        for index in range(n):
            os.chdir(os.path.dirname(os.getcwd()))

    with open(yaml_file, 'r', encoding='utf-8') as f_structure:
        line = f_structure.readline()
        folder_level = 0
        correct_name = line.strip('- :\n')
        os.mkdir(correct_name)
        line_before = correct_name
        for line in f_structure:
            stripped_line = line.strip('- :\n')
            if line.endswith(':\n'):
                if line.index('-') // 4 == folder_level:
                    os.mkdir(stripped_line)
                elif line.index('-') // 4 > folder_level:
                    os.chdir(os.path.join(os.getcwd(), line_before))
                    os.mkdir(stripped_line)
                    folder_level += 1
                else:
                    up_by_tree(folder_level - (line.index('-') // 4))
                    os.mkdir(stripped_line)
                    folder_level = line.index('-') // 4
                line_before = stripped_line
            else:
                if line.index('-') // 4 == folder_level:
                    open(stripped_line, 'w').close()
                elif line.index('-') // 4 > folder_level:
                    os.chdir(os.path.join(os.getcwd(), line_before))
                    open(stripped_line, 'w').close()
                    folder_level += 1
                else:
                    up_by_tree(folder_level - (line.index('-') // 4))
                    open(stripped_line, 'w').close()
                    folder_level = line.index('-') // 4


exit(main(sys.argv))
# Не знаю, как сделать так, чтобы можно было добавить одну папку или файл в конфиг,
# снова запустить скрипт и не вылетало ошибки
# Мои варианты: 1 - везде вставлять if not exist, но долго и очень раздувает код,
# 2 - это невозможно сделать в модуле os.
# Зато хоть потренировалась с терминалом.
