"""
Задание 1. Спортсмен занимается ежедневными пробежками.В первый день его
результат составил a километров. Каждый день спортсмен увеличивал результат
на 10 % относительно предыдущего. Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
"""

day_res = float(input("Введите результат первого дня в км: "))
final_res = float(input("Введите цель в км: "))
count = 1
sum_res = day_res
print()
print("ЖУРНАЛ ТРЕНИРОВОК:")
while sum_res <= final_res:
    print(
        f"{count} день. Сегодня {round(day_res, 2)} км. "
        f"Всего {round(sum_res, 2)} км.")
    day_res *= 1.1
    sum_res += day_res
    count += 1
print(
    f"{count} день. Сегодня {round(day_res, 2)} км. "
    f"Всего {round(sum_res, 2)} км. Результат достигнут!")
