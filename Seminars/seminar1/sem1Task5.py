# Задача №5. Решение в группах Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

num_start = int(input("Какой по счету вагон с головы поезда: "))
num_carriage = int(input("Номер вагона поезда: "))

if num_start != num_carriage:
    print("Кол-во вагонов в поезде:", (num_carriage + num_start - 1))
else:
    print("Нужно чуть больше информации")