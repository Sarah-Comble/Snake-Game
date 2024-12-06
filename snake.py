from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) :
        self.segments = []
        self.create_snake()

    def create_snake(self) :
        for position in  POSITION:
            self.add_segment(position)

    def add_segment(self, position ) :
        new_segment = Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        # new_segment.setx(x)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # pour avoir une belle animation, il faut que le bloc n°3 prenne la place du 2 et le 2 du premier
            # on prend le nb total de turtle comme start, 0 (1er pos de la liste) comme end, et une différence de -1 pour aller à l'envers
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)  # on a pris les coord. du premier bloc puis on le met dans le bloc en cours afin de le bouger
        self.segments[0].forward(MOVE_DISTANCE)  # maintenant on bouge la tête

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()