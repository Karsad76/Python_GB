"""Задача 18. Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X
"""

s = input("Введите элементы массива через пробел: ")
array = [int(x) for x in s.split()]
search_num = int(input("Введите искомое число: "))

min_diff_index = array.index(max(array))
min_diff = abs(abs(max(array)) - abs(search_num))

for i in array:
    a = abs(abs(i) - abs(search_num))

    if a < min_diff:
        min_diff = a
        min_diff_index = array.index(i)

print(f"Самое близкое число к заданному: {array[min_diff_index]}")
print(array)
