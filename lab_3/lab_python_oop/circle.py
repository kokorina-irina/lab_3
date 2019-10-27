import math
from lab_python_oop import geometric_shape, color_shape


class Circle(geometric_shape.Geometric_shape):
    name: str = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.class_color = color_shape.Color_shape(color)

    def area(self):
        return math.pi * self.radius * self.radius

    def __repr__(self):
        return "Радиус: {}, " \
               " Цвет: {}," \
               " Площадь: {}".\
            format(self.radius,
                   self.class_color.color,
                   self.area())

    def get_name(self):
        return self.name
