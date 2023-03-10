"""
Задача 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
"""

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

seasons = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
           7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень",
           12: "Зима"}

month = int(input("Введите номер месяца: "))
if month in range(1, 12):

    print("Результат через список: ", end='')
    if month in winter:
        print('Зима')
    elif month in spring:
        print('Весна')
    elif month in summer:
        print('Лето')
    elif month in autumn:
        print('Осень')

    print("Результат через словарь: ", end='')
    print(seasons[month])
else:
    print("Номер месяца должен быть в диапазоне 1-12")
