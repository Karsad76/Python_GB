"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через
перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"salary": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name, s_name, pos, sal, bon):
        self.name = name
        self.surname = s_name
        self.position = pos
        self._income = {"salary": sal, "bonus": bon}

    def __str__(self):
        s = self._income["salary"]
        b = self._income["bonus"]
        return (f"{self.name} {self.surname}, {self.position}, "
                f"доход: {s + b}")

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        s = self._income["salary"]
        b = self._income["bonus"]
        print(f"Полный доход: {s + b}")


employee1 = Position("Сергей", "Иванов", "директор", 1000, 2000)
employee2 = Position("Иван", "Сергеев", "менеджер", 100, 200)
employee3 = Position("Ирина", "Петрова", "бухгалтер", 500, 700)

employee1.get_full_name()
employee1.get_total_income()
print()
employee2.get_full_name()
employee2.get_total_income()
print()
employee3.get_full_name()
employee3.get_total_income()
print()
print(employee1)
print(employee2)
print(employee3)
