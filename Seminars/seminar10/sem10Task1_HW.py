"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор
кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
import json

words = ['разработка', 'сокет', 'декоратор']

for i in words:
    print(i, type(i))

    # var.1 encode/decode literal to unicode code points
    a = i.encode('unicode-escape').decode('utf-8')
    print(f"encode/decode: {a}, {type(a)}, "
          f"{a.encode('utf-8').decode('unicode-escape')}")

    # var.2 encode/decode literal to unicode code points (via JSON module)
    b = json.dumps(i)
    print(f'JSON-string:  {b}, {type(b)}, {json.loads(b)}')
    print()
