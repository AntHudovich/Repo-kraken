import os
import shutil
# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
# например, во фреймворке django.


def copy_templates(root_directory):
    for path, directories, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.html'):
                new_path = os.path.join(os.path.join(root_directory, 'templates'), os.path.basename(path))
                if not os.path.exists(new_path):
                    os.makedirs(new_path)

                shutil.copyfile(os.path.join(path, file), os.path.join(new_path, file))


if __name__ == '__main__':
    copy_templates('C:/Users/tosha/PycharmProjects/pythonProject/Hudovich_Antanina_dz_7/my_project_7_3')
# Сама написала, но через папки с названием templates и shutil.copytree(), работало,
# но создавались лишние дублирующие подпапки templates. Победить эту гадость не удалось.
# Поэтому в итоге решила разобраться с твоим примером.
# Возник вопрс можно ли использовать неполный путь в root_directory?
