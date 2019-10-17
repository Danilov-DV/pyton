"""
1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(var1, var2):
    """
    Ф-ция деления 2 чисел
    :param var1: float
    :param var2:  float
    :return: float
    """
    return var1 / var2


user_var1 = input('Делимое ')
user_var2 = input('Делитель ')

try:
    print(f"Результат = {my_func(float(user_var1), float(user_var2))}")
except ValueError as e:
    print("Ошибка ввода")
except ZeroDivisionError as e:
    print("Деление на 0")
