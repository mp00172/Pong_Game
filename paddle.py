from turtle import Turtle
from config import *


class Paddle(Turtle):
	def __init__(self, x_position, y_up_limit, y_dn_limit):
		super().__init__()
		self.y_up_limit = y_up_limit
		self.y_dn_limit = y_dn_limit
		self.penup()
		self.speed(0)
		self.hideturtle()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=0.5)
		self.goto(x=x_position, y=0)
		self.showturtle()

	def get_position(self):
		return self.position()

	def move_up(self):
		if self.ycor() < self.y_up_limit - PADDLE_Y_OFFSET:
			self.goto(x=self.xcor(), y=self.ycor() + PADDLE_MOVE_STEP_PLAYER)
		else:
			self.goto(x=self.xcor(), y=self.y_up_limit - PADDLE_Y_OFFSET)

	def move_down(self):
		if self.ycor() > self.y_dn_limit + PADDLE_Y_OFFSET:
			self.goto(x=self.xcor(), y=self.ycor() - PADDLE_MOVE_STEP_PLAYER)
		else:
			self.goto(x=self.xcor(), y=self.y_dn_limit + PADDLE_Y_OFFSET)

	def comp_paddle_move(self, ball_position):
		if ball_position[1] > self.ycor():
			if self.ycor() < self.y_up_limit - PADDLE_Y_OFFSET:
				self.goto(x=self.xcor(), y=self.ycor() + PADDLE_MOVE_STEP_COMP)
		else:
			if self.ycor() > self.y_dn_limit + PADDLE_Y_OFFSET:
				self.goto(x=self.xcor(), y=self.ycor() - PADDLE_MOVE_STEP_COMP)
