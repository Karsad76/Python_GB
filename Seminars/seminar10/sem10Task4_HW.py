"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for i in words:
    print(i, type(i))

    a = i.encode('unicode-escape')
    print(a, {type(a)})

    a = a.decode('unicode-escape')
    print(a, {type(a)})
    print()
