#!/usr/bin/env python
# -*- coding: utf-8

import sys

class Triangle():
    REGULAR = 0
    ISOSCELES = 1
    EQUILATERAL = 2

    def __init__(self, a, b, c):
        assert isinstance(a, (int, long)), "стороны должны быть целыми числами"
        assert isinstance(b, (int, long)), "стороны должны быть целыми числами"
        assert isinstance(c, (int, long)), "стороны должны быть целыми числами"

        assert a > 0, "стороны должны быть положительными"
        assert b > 0, "стороны должны быть положительными"
        assert c > 0, "стороны должны быть положительными"

        assert a + b > c, "не бывает треугольника с такими сторонами"
        assert a + c > b, "не бывает треугольника с такими сторонами"
        assert b + c > a, "не бывает треугольника с такими сторонами"

        self.a = a
        self.b = b
        self.c = c


    @property
    def type(self):
        if self.a == self.b and self.b == self.c:
            return Triangle.EQUILATERAL
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return Triangle.ISOSCELES
        else:
            return Triangle.REGULAR


def main():
    data = sys.stdin.readlines()
    assert len(data) == 1, "числа должны быть на одной строке"
    x, y, z = map(int, data[0].split())
    triangle = Triangle(x, y, z)
    if triangle.type == Triangle.REGULAR:
        print("Обычный треугольник")
    elif triangle.type == Triangle.ISOSCELES:
        print("Равнобедренный треугольник")
    elif triangle.type == Triangle.EQUILATERAL:
        print("Равносторонний треугольник")
    else:
        return 1

if __name__ == '__main__':
    sys.exit(main())
