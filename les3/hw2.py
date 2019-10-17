"""
2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

user_name = input('имя ')
user_surname = input('фамилия ')
user_year = input('год рождения ')
user_email = input('email ')
user_phone = input('телефон ')


def my_func(var_name, var_surname, var_year, var_email, var_phone):
    """
    выводит данные о пользователе в одну строку
    :param var_name: str
    :param var_surname: str
    :param var_year: str
    :param var_email: str
    :param var_phone: str
    :return: 
    """
    print(f"{var_surname} {var_name}, {var_year} г.р., email: {var_email}, телефон: {var_phone}")


my_func(var_email=user_email, var_name=user_name, var_surname=user_surname, var_year=user_year, var_phone=user_phone)
