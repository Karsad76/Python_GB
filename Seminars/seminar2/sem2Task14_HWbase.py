"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""

n = int(input("Введите натуральное число: "))
i = 0
list = []
while 2 ** i <= n:
    # print(2 ** i)
    list.append(2 ** i)
    i += 1
print(*list)
