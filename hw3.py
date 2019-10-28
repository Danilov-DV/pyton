"""
Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
surname, position ( должность), income ( доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"profit": profit, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
дохода с учетом премии ( get_full_profit) . Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    __income = {"profit": 0, "bonus": 0}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def set_income(self, profit, bonus):
        self.__income["profit"] = profit
        self.__income["bonus"] = bonus

    def get_income(self):
        return self.__income


class Position(Worker):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        _ = self.get_income()
        return self.get_income()["profit"] + self.get_income()["bonus"]


my_worker = Position(name="Ivan", surname="Ivanov")
my_worker.set_income(20000, 5000)

print(my_worker.get_full_name())
print(my_worker.get_full_profit())
