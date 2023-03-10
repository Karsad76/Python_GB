"""
Задание 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
Решите через рекурсию. В задании нельзя применять циклы.
Допускается исп-е встроенных ф-ций
"""


def print_ascii_table(index):
    if index < 128:
        if (index - 32) % 10 == 0:
            print()
        print(f"{index:3}-{chr(index)}", end=' ')
        print_ascii_table(index + 1)
    else:
        return


start_index = 32
print_ascii_table(start_index)
