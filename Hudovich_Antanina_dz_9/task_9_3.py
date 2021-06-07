# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


if __name__ == '__main__':
    salary_components = {
        "wage": 1000,
        "bonus": 100
    }

    ringleader = Position('Vasiliy', 'Chapaev', 'commander', salary_components)
    ringleader.get_full_name()
    ringleader.get_total_income()

    assistant = Position('Peter', 'Isaev', 'assistant', salary_components)
    assistant.get_full_name()
    assistant.get_total_income()

    fighting_girlfriend = Position('Ann', 'the_machine_gunner', 'mastermind', salary_components)
    fighting_girlfriend.get_full_name()
    fighting_girlfriend.get_total_income()

# А total_income у всех одинаковый потому что коммунизьм
