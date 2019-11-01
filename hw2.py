"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class DivZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_a = input("Введите делимое: ")
inp_b = input("Введите делитель: ")

try:
    inp_a = int(inp_a)
    inp_b = int(inp_b)
    if inp_b == 0:
        raise DivZeroError("Деление на 0!")
except ValueError:
    print("Вы ввели не число")
except DivZeroError as e:
    print(e)
else:
    print(f"Результат: {inp_a / inp_b}")

print("...")
