from tkinter import Tk, Canvas


class CanvasGen:

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        window = Tk()
        self.canvas = Canvas(window, height=height, width=width, bg=color)

    def rectangle(self):
        x1 = int(input("Enter x of rectangle: "))
        y1 = int(input("Enter y of rectangle: "))
        y2 = int(input("Enter height of rectangle: ")) + y1
        x2 = int(input("Enter width of rectangle: ")) + x1
        color = input("Enter color of rectangle: ")
        self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)

    def square(self):
        x1 = int(input("Enter x of square: "))
        y1 = int(input("Enter y of square: "))
        side = int(input("Enter side of square: "))
        color = input("Enter color of square: ")
        self.canvas.create_rectangle(x1, y1, x1+side, y1+side, fill=color)
