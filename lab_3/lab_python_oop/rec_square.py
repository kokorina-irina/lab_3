from lab_python_oop import rectangle, color_shape


class Square(rectangle.Rectangle):
    name: str = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)
        self.side = side
        self.class_color = color_shape.Color_shape(color)

    def area(self):
        return self.side * self.side

    def __repr__(self):
        return "Сторона: {}, " \
               " Цвет: {}," \
               " Площадь: {}".\
            format(self.side,
                   self.class_color.color,
                   self.area())

    def get_name(self):
        return self.name
