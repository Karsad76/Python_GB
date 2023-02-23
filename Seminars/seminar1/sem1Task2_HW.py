# Задача 2: Найдите сумму цифр трехзначного числа.

# geting input data
num = abs(int(input("Введите любое 3х значное число: ")))

# checking numbers of digits and output the sum of its
if 99 < abs(num) < 1000:
    sum = round(num % 10 + ((num % 100 - num % 10) / 10) +
                (num % 1000 - num % 100) / 100)
    print(f'Сумма цифр числа {num} = {sum}')
else:
    print(f"Введенное число {num} не 3х значное")
