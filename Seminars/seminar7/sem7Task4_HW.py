"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
"""


class Matrix():

    def __init__(self, arr):
        self.mtrx = arr

    def __str__(self):
        for i in self.mtrx:
            print(i)
        return ""

    def __add__(self, other):
        res_mtrx = []
        for sublist in zip(self.mtrx, other):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            res_mtrx.append(temp)

        for r in res_mtrx:
            print(r)
        return ""


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1)
print(m1 + [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
