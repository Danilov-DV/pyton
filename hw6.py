'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''


from itertools import count
from itertools import cycle


def func_a(start_):
    for el in count(start_):
        yield el


def func_b(list_):
    for el in cycle(list_):
        yield el


my_gen = func_a(7)
for i in range(20):
    print(next(my_gen))

my_gen = func_b(["abc", 123, "a", 6])
for i in range(20):
    print(next(my_gen))


