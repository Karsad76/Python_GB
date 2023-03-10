"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def calculate_digits(n):
    count_even = count_odd = 0
    if n > 1:
        if n % 10 % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return calculate_digits(n // 10)
    else:
        return count_even, count_odd


input_num = int(input("Введите натуральное число: "))
counts = calculate_digits(input_num)
print(f"Четных цифр - {counts[0]}, нечетных - {counts[1]}")

