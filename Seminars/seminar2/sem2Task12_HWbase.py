"""
Задача 12: Петя задумывает два натуральных числа X и Y (X,Y ≤ 1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет
сумму этих чисел S и их произведение P. Нужно отгадать задуманные Петей числа
"""

s = int(input("Сумма чисел? "))
p = int(input("Произведение чисел? "))

for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(f"Загаданные числа: {i} и {j}")
