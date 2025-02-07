from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        if self.radius < 0:
            return 0
        return pi * self.radius ** 2
    def perimeter(self):
        if self.radius < 0:
            return 0
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
