"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""

num = int(input("Введите число: "))
degree = int(input("Введите степень числа: "))


def degree_calc_rec(arg1, arg2):
    if arg2 == 1:
        return arg1
    else:
        return arg1 * degree_calc_rec(arg1, arg2 - 1)


print(f"{num}**{degree} = {degree_calc_rec(num, degree)}")
