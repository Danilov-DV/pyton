"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    __total_consumption = 0

    def __init__(self, value):
        Clothes.__total_consumption += value

    @property
    def clothes_consumption(self):
        return self.__total_consumption

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size
        super().__init__(self.consumption)

    @property
    def consumption(self):
        return 2 * self.size + 0.3


class Costume(Clothes):

    def __init__(self, height):
        self.height = height
        super().__init__(self.consumption)

    @property
    def consumption(self):
        return self.height / 6.5 + 0.5


coat1 = Coat(1)
print(coat1.consumption)
print(coat1.clothes_consumption)
print()

coat2 = Coat(2)
print(coat2.consumption)
print(coat1.clothes_consumption)
print(coat2.clothes_consumption)
print()

costume1 = Costume(1.85)
print(costume1.consumption)
print(costume1.clothes_consumption)




