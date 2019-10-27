from lab_python_oop import rectangle, circle, rec_square


def main():
    test_rectangle = rectangle.Rectangle(2, 3, "синий")
    test_circle = circle.Circle(5, "зелёный")
    test_square = rec_square.Square(5, "красный")

    print(test_rectangle.get_name(), end="\n")
    print(test_rectangle)
    print(test_circle.get_name(), end="\n")
    print(test_circle)

    print(test_square.get_name(), end=":\n")
    print(test_square)


if __name__ == "__main__":
    main()
