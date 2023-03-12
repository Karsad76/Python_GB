"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
заданного максимума)
"""

import random

rand_list = []
n = 100
for i in range(n):
    rand_list.append(random.randint(-100, 100))
print(rand_list)

min_num = int(input("Введите нижнюю границу диапазона: "))
max_num = int(input("Введите верхнюю границу диапазона: "))
for i in rand_list:
    if min_num <= i <= max_num:
        print(i, end=' ')
