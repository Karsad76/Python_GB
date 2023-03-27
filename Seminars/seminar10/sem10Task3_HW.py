"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode
decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

words = ["attribute", "класс", "функция", "type"]

for i in words:
    try:
        a = bytes(i, 'ascii')
        print(a, type(a), len(a))
    except UnicodeEncodeError:
        print(f"'{i}' нельзя записать в байтовом формате с префиксом b'")
