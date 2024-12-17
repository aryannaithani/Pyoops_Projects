import turtle
from random import randint

class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def is_in_rectangle(self):
        min_x = min(obj1.c1[0], obj1.c2[0])
        max_x = max(obj1.c1[0], obj1.c2[0]) + 1
        min_y = min(obj1.c1[1], obj1.c2[1])
        max_y = max(obj1.c1[1], obj1.c2[1]) + 1
        if self.x in range(min_x, max_x) and self.y in range(min_y, max_y):
            print(True)
        else:
            print(False)


class Rectangle:

    def __init__(self):
        self.c1 = randint(0, 100), randint(0, 100)
        self.c2 = randint(0, 100), randint(0, 100)
        self.area = int(abs(self.c1[0] - self.c2[0]) * abs(self.c1[1] - self.c2[1]))
        print(f"Corners of the Rectangle are {self.c1} and {self.c2}")

    def area_is_correct(self):
        if self.area == z:
            print(True)
        else:
            print(False)
            print(f"You were off by {abs(self.area - z)}")


class Graphics:

    def __init__(self):
        self.my_turtle = turtle.Turtle()

    def plot_rectangle(self):
        self.my_turtle.penup()
        self.my_turtle.goto(obj1.c1[0], obj1.c1[1])
        self.my_turtle.pendown()
        self.my_turtle.goto(obj1.c1[0], obj1.c2[1])
        self.my_turtle.goto(obj1.c2[0], obj1.c2[1])
        self.my_turtle.goto(obj1.c2[0], obj1.c1[1])
        self.my_turtle.goto(obj1.c1[0], obj1.c1[1])

    def plot_point(self):
        self.my_turtle.color()
        self.my_turtle.penup()
        self.my_turtle.goto(x, y)


obj1 = Rectangle()
x = int(input("Guess x Co-ords: "))
y = int(input("Guess y Co-ords: "))
z = int(input("Guess Area: "))
obj2 = Point(x, y)
obj2.is_in_rectangle()
obj1.area_is_correct()
obj3 = Graphics()
obj3.plot_rectangle()
obj3.plot_point()
turtle.done()