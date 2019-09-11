import math


class Apple:
    def __init__(self, c, w, t, co, ):
        self.color = c
        self.weight = w
        self.taste = t
        self.county = co


app = Apple(10, 3, 4, 5)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius * math.pi


ci = Circle(10)


class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2


tri = Triangle(10, 15)


class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6


hexi = Hexagon(10)
print(hexi.calculate_perimeter())