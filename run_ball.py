import turtle
from ball import Ball
from seven_segments_proc import SevenSegmentProc
import random

class BallSimulation:
    def __init__(self, num_ball, delay_in_seconds, dt:int=1):
        self.__delay_in_seconds = delay_in_seconds
        self.__dt = dt
        
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.__canvas_width = turtle.screensize()[0]
        self.__canvas_height = turtle.screensize()[1]
        print(self.__canvas_width, self.__canvas_height)
        self.__ball_list = []
        self.__num_ball = num_ball

    def __create_ball(self):
        for i in range(self.__num_ball):
            ball_radius = 0.05 * self.__canvas_width
            x = (random.randint(-1*self.__canvas_width + ball_radius, self.__canvas_width - ball_radius))
            y = (random.randint(-1*self.__canvas_height + ball_radius, self.__canvas_height - ball_radius))
            vx = (2*random.uniform(-1.0, 1.0))
            vy = (2*random.uniform(-1.0, 1.0))
            color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.__ball_list.append(Ball(ball_radius, x, y, vx, vy, color, self.__canvas_width, self.__canvas_height))
        print(self.__ball_list)

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.__canvas_width, -self.__canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.__canvas_width)
            turtle.left(90)
            turtle.forward(2*self.__canvas_height)
            turtle.left(90)

    def run(self):
        self.__create_ball()
        Seven_Seg = SevenSegmentProc(turtle.Turtle(), (255, 0, 0))
        i = 0
        while (True):
            turtle.clear()
            self.__draw_border()
            for ball in self.__ball_list:
                ball.draw_ball()
                ball.move_ball(self.__dt)
                ball.update_ball_velocity()
            turtle.update()

            Seven_Seg.clear()
            Seven_Seg.draw(i%10)
            Seven_Seg.my_delay(self.__delay_in_seconds)
            
            turtle.update()
            
            i+= 1

BallSimulation(num_ball=5, delay_in_seconds=0.2, dt=5).run()

turtle.done()
