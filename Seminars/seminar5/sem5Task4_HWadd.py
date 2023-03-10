"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""

n = int(input(
    'Введите кол-во элементов последовательности "1 -0.5 0.25 -0.125 ...": '))


def sum_calculate(arg1):
    if arg1 == 1:
        return 1
    else:
        return 1 + (1 / -2 * sum_calculate(arg1 - 1))


print(f"Кол-во элементов: {n}. Их сумма = {sum_calculate(n)}")
