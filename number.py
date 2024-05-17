class Number:
    def __init__(self, num):
        self._num = num

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, n):
        self._num = n

    def __add__(self, other):
        return Number(self._num + other.num)

    def __mul__(self, other):
        return Number(self._num * other.num)

    def __floordiv__(self, other):
        return Number(self._num / other.num)

    def __sub__(self, other):
        return Number(self._num - other.num)

    def __mod__(self, other):
        return Number(self._num % other.num)

    def __str__(self):
        return f": {self._num}"

n1 = Number(15)
n2 = Number(4)
n1.num = 5
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)
print(n1 % n2)

class UNumber(Number):
    def __init__(self, n):
        super().__init__(n)
    
    @property
    def  num(self):
        return self._num

    @num.setter
    def num(self, n):
        if n < 0:
            self._num = 1
        else:
            self._num = n
n = UNumber(25)
n.num = -13
print(n)
print(n2 + n)
