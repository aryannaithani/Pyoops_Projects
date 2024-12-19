from MathPainter.generator import CanvasGen

canvas_height = int(input("Enter height of canvas: "))
canvas_width = int(input("Enter width of canvas: "))
canvas_color = tuple(map(int, input("Enter RGB values for background color of canvas: ").split()))

obj1 = CanvasGen(canvas_height, canvas_width, canvas_color)

while True:
    command = input("What do you want to draw: ")
    if command == 'square':
        obj1.square()
    elif command == 'rectangle':
        obj1.rectangle()
    else:
        obj1.save_as_png('output.png')
        break