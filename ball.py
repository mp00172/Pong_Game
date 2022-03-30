from turtle import Turtle
import random
from config import *


class Ball(Turtle):
	def __init__(self, x_left, x_right, y_up, y_dn):
		super().__init__()
		self.playground_x_left = x_left
		self.playground_x_right = x_right
		self.playground_y_up = y_up
		self.playground_y_dn = y_dn
		self.shape("circle")
		self.penup()
		self.color("red")
		self.shapesize(stretch_wid=0.7, stretch_len=0.7)
		self.speed(0)

	def move(self):
		if self.heading() < 0:
			self.setheading(self.heading() + 360)
		elif self.heading() > 360:
			self.setheading(self.heading() - 360)
		if not self.scored():
			if self.wall_bounce():
				self.setheading(-self.heading())
			self.forward(BALL_STEP)

	def get_position(self):
		return self.position()

	def serve_to_left(self):
		self.goto(0, 0)
		self.setheading(random.randint(125, 235))
		self.move()

	def serve_to_right(self):
		self.goto(0, 0)
		self.setheading(random.randint(-55, 55))
		self.move()

	def wall_bounce(self):
		if self.ycor() >= self.playground_y_up or self.ycor() <= self.playground_y_dn:
			return True
		return False

	def scored(self):
		if self.xcor() >= self.playground_x_right or self.xcor() <= self.playground_x_left:
			return True
		return False

	def check_point_winner(self):
		if self.xcor() >= self.playground_x_right:
			return "left"
		elif self.xcor() <= self.playground_x_left:
			return "right"







