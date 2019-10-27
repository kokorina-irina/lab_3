from lab_python_oop import geometric_shape, color_shape


class Rectangle(geometric_shape.Geometric_shape):
    name: str = "Прямоугольник"

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.class_color = color_shape.Color_shape(color)

    def area(self):
        return self.width * self.length

    def __repr__(self):
        return "Длина: {}, " \
               "Ширина: {}," \
               " Цвет: {}," \
               " Площадь: {}". \
            format(self.length,
                   self.width,
                   self.class_color.color,
                   self.area())

    def get_name(self):
        return self.name
