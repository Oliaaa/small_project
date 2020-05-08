class Fraction:

    """Класс для работы с дробями."""

    # a - числитель, b - знаменатель
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Вывод дроби
    def __str__(self):
        return ('Дробь: {}/{}'.format(self.a, self.b))

    # Нахождение Наибольшего общего делителя для числителя и знаменателя
    @staticmethod
    def NOD(self):
        i = 2
        nod = 1
        while i <= self.a or i <= self.b:
            if self.a % i == 0 and self.b % i == 0:
                nod = i
            i += 1
        return Fraction(self.a // nod, self.b // nod)

    # Сложение дробей
    def __add__(self, other):
        if isinstance(other, Fraction):
            if other.b != self.b:
                summa = Fraction(((self.a * other.b) + (other.a * self.b)), (self.b * other.b))
                return Fraction.NOD(summa)
                '''if self.b % other.b == 0:
                    summa = Fraction(self.a + other.a * (self.b // other.b), self.b)
                    return Fraction.NOD(summa)

                elif other.b % self.b == 0:
                    summa = Fraction(other.a + self.a * (other.b // self.b), other.b)
                    return Fraction.NOD(summa)
                else:
                    i = 2
                    M = max(self.b, other.b) * i
                    while (M % self.b != 0) or (M % other.b != 0):
                        M *= i
                        i += 1
                    summa = Fraction((self.a * (M // self.b) + (other.a * (M // other.b))), M)
                    return Fraction.NOD(summa)'''
            else:
                summa = Fraction(self.a + other.a, self.b)
                return Fraction.NOD(summa)
                #if summa.a == summa.b:
                #    return 1
        elif isinstance(other, int):
            #return Fraction(self.a + other * self.b, self.b)
            summa = Fraction(self.a + other * self.b, self.b)
            return Fraction.NOD(summa)

    # Вычитание дробей
    def __sub__(self, other):
        if isinstance(other, Fraction):
            if other.b != self.b:
                res = Fraction(((self.a * other.b) - (other.a * self.b)), (self.b * other.b))
                return Fraction.NOD(res)
            else:
                res = Fraction(self.a - other.a, self.b)
                return Fraction.NOD(res)
        elif isinstance(other, int):
            res = Fraction(self.a - other * self.b, self.b)
            return Fraction.NOD(res)

    # Умножение дробей
    def __mul__(self, other):
        if isinstance(other, Fraction):
            res = Fraction(self.a * other.a, self.b * other.b)
            return Fraction.NOD(res)
        elif isinstance(other, int):
            res = Fraction(self.a * other, self.b)
            return Fraction.NOD(res)

    # Приведение дроби к целому числу
    def __int__(self):
        if self.a < self.b:
            return 0
        elif self.a == self.b:
            return 1
        elif self.a % self.b == 0:
            return self.a // self.b
        else:
            return self.a % self.b

    # Приведение дроби к числу с плавающей точкой
    def __float__(self):
        return self.a / self.b

class OperationsOnFraction(Fraction):
    def getint(self):
        return self.a // self.b

    def getfloat(self):
        return self.a / self.b

n = Fraction(18, 5)
print(n)
print(float(n))
print(OperationsOnFraction.getint(n))

m = Fraction(2, 3)
print(m)
print(int(m))

print(n + m)
print(n - m)
print(n * m)
print(n + 2)
print(n * 2)


