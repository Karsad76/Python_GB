"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""

n = int(input("Введите натуральное число: "))
i = 0
l = []
while 2 ** i <= n:
    # print(2 ** i)
    l.append(2 ** i)
    i += 1
print(f"Степени 2 до {n}:", *l)
