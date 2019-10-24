'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''


def my_generator(list_):
    i = 0
    for _ in list_:
        if i > 0 and list_[i] > list_[i - 1]:
            yield list_[i]
        i += 1


my_list = [1, 2, 7, 6, 5]
results_list = [el for el in my_generator(my_list)]

assert results_list == [2, 7], f"[2, 7] = {results_list}"
