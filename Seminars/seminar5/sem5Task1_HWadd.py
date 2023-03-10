"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def calculator():
    operation = input("Введите действие: + - * / ** или 0 для выхода: ")

    if operation == "0":
        print("Конец программы")
        return
    else:
        if operation in "+-*/**":
            try:
                arg1 = int(input("Первое число: "))
                arg2 = int(input("Второе число: "))

                if operation == "+":
                    print(f"{arg1} + {arg2} = {arg1 + arg2}")
                    return calculator()

                elif operation == "-":
                    print(f"{arg1} - {arg2} = {arg1 - arg2}")
                    return calculator()

                elif operation == "*":
                    print(f"{arg1} * {arg2} = {arg1 * arg2}")
                    return calculator()

                elif operation == "**":
                    print(f"{arg1} ** {arg2} = {arg1 ** arg2}")
                    return calculator()

                elif operation == "/":
                    try:
                        arg1 / arg2
                    except ZeroDivisionError:
                        print("На 0 делить нельзя!")
                    else:
                        print(f"{arg1} / {arg2} = {arg1 / arg2}")
                    finally:
                        return calculator()

            except ValueError:
                print("Введите число, не строку. Попробуйте еще раз.")
                return calculator()


calculator()
