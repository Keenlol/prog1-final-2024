
class SevenSegmentProc:

    def __init__(self, my_turtle, color):
        self.__my_turtle = my_turtle
        self.__color = color

        self.__my_turtle.color(self.__color)
        self.__my_turtle.penup()
        self.__my_turtle.setheading(0)
        self.__my_turtle.goto(0, 0)
        self.__my_turtle.pensize(10)
        self.__my_turtle.hideturtle()
    
    
    def draw(self, digit):
        if digit == 0:
            self.__my_turtle.goto(-50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.penup()
    
        if digit == 1:
            self.__my_turtle.goto(50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.penup()
    
        if digit == 2:
            self.__my_turtle.goto(-50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.penup()
    
        if digit == 3:
            self.__my_turtle.goto(-50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(-100)
            self.__my_turtle.left(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.left(90)
            self.__my_turtle.penup()
    
        if digit == 4:
            self.__my_turtle.goto(-50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(-100)
            self.__my_turtle.forward(-100)
            self.__my_turtle.right(90)
            self.__my_turtle.penup()
    
        if digit == 5:
            self.__my_turtle.goto(-50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(-100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.left(90)
            self.__my_turtle.penup()
    
        if digit == 6:
            self.draw(5)
            self.__my_turtle.goto(-50, 0)
            self.__my_turtle.pendown()
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.penup()
        
        if digit == 7:
            self.__my_turtle.goto(-50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.forward(100)
            self.__my_turtle.forward(-100)
            self.draw(1)
    
        if digit == 8:
            self.draw(0)
            self.__my_turtle.goto(-50, 0)
            self.__my_turtle.pendown()
            self.__my_turtle.forward(100)
            self.__my_turtle.penup()
    
        if digit == 9:
            self.draw(5)
            self.__my_turtle.goto(50, 100)
            self.__my_turtle.pendown()
            self.__my_turtle.right(90)
            self.__my_turtle.forward(100)
            self.__my_turtle.left(90)
            self.__my_turtle.penup()
    
    def clear(self):
        self.__my_turtle.clear()
    
    def my_delay(self, dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass


