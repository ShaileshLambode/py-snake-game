from turtle import Turtle, Screen

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.position1 = (0,0)

    def create_snake(self):
        for position in starting_pos:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def expand(self):
        self.add_segment(self.segment[-1].position())

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def move_snake(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(move_distance)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
