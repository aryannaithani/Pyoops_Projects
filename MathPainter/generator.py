from PIL import Image
import numpy as np


class CanvasGen:

    def __init__(self, height, width, color):
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = color

    def rectangle(self):
        x1 = int(input("Enter x of rectangle: "))
        y1 = int(input("Enter y of rectangle: "))
        height = int(input("Enter height of rectangle: ")) + y1
        width = int(input("Enter width of rectangle: ")) + x1
        color = tuple(map(int, input("Enter RGB values for color of rectangle: ").split()))
        self.data[x1:height, y1:width] = color

    def square(self):
        x1 = int(input("Enter x of square: "))
        y1 = int(input("Enter y of square: "))
        side = int(input("Enter side of square: "))
        color = tuple(map(int, input("Enter RGB values for color of square: ").split()))
        self.data[x1:x1+side, y1:y1+side] = color

    def save_as_png(self, name):
        img = Image.fromarray(self.data, 'RGB')
        img.save(name)