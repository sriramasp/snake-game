from turtle import Turtle

move = 15
direction = 90
starting_postitons = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.snake = []
        self.create_segment()

    def create_segment(self):
        for position in starting_postitons:
           self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color()
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move_segment(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(move)

    def up(self):
        if self.snake[0].heading() != direction*3:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != direction:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != direction * 2:
            self.snake[0].setheading(0)

