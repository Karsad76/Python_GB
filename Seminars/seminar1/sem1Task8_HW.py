# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).

# input data prompt
m = int(input("Длина шоколодки: "))
n = int(input("Ширина шоколодки: "))
k = int(input("Сколько долек нужно отломить: "))

# output result
if k % m == 0 or k % n == 0:
    print(f'От шоколадки размером {m}x{n} можно отломить '
          f'{k} долек за один разлом')
else:
    print(f'От шоколадки размером {m}x{n} нельзя отломить '
          f'{k} долек за один разлом')
