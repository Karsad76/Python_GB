"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping_site(args):
    p_site = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in p_site.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


ping_site(['ping', 'yandex.ru'])
ping_site(['ping', 'youtube.com'])
