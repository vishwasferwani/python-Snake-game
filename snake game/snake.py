from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP  = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()

    def create_snake(self):
        for pos in POSITIONS:
            self.new_turtle(pos)

    def new_turtle(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)

    def increase_snake(self):
        self.new_turtle(self.all_turtle[-1].position())
    def move(self):
        for seg_num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[seg_num - 1].xcor()
            new_y = self.all_turtle[seg_num - 1].ycor()
            self.all_turtle[seg_num].goto(new_x, new_y)

        self.all_turtle[0].forward(20)

    def up(self):
        if self.all_turtle[0].heading()!= DOWN:
            self.all_turtle[0].setheading(UP)

    def down(self):
        if self.all_turtle[0].heading() != UP:
            self.all_turtle[0].setheading(DOWN)

    def right(self):
        if self.all_turtle[0].heading() != LEFT:
            self.all_turtle[0].setheading(RIGHT)

    def left(self):
        if self.all_turtle[0].heading() != RIGHT:
            self.all_turtle[0].setheading(LEFT)

