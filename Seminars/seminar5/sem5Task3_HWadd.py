"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def flip_number(n):
    if n > 1:
        print(n % 10, end="")
        if n // 10 > 0:
            flip_number(n // 10)
    else:
        print(n)


input_num = int(input("Введите натуральное число: "))
flip_number(input_num)
