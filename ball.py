import turtle
class Ball:
    def __init__(self, size, x, y, vx, vy, color, canvas_width, canvas_height):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.__canvas_width = canvas_width
        self.__canvas_height = canvas_height
        
    def draw_ball(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y-self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, dt):
        self.x += self.vx*dt
        self.y += self.vy*dt


    def update_ball_velocity(self):
        if abs(self.x) > (self.__canvas_width - self.size):
            self.vx = -self.vx
    
        if abs(self.y) > (self.__canvas_height - self.size):
            self.vy = -self.vy
