# Задача 2: Найдите сумму цифр трехзначного числа.

# geting input data
num = abs(int(input("Введите любое 3х значное число: ")))

# checking numbers of digits and output the sum of its
if 99 < abs(num) < 1000:
    print(int(num % 10 + ((num % 100 - num % 10) / 10) +
          (num % 1000 - num % 100) / 100))
else:
    print("Введенное число не 3х значное")
