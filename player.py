from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)

    def detect_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False