from turtle import Turtle
from config import *


class Scoreboard(Turtle):
	def __init__(self, imp_height):
		super().__init__()
		self.player_left_score = 0
		self.player_right_score = 0
		self.y_position = imp_height // 2 - 80
		self.hideturtle()
		self.speed(0)
		self.color("blue")
		self.penup()
		self.goto(x=-35, y=self.y_position)
		self.write(f"{self.player_left_score}", align="right", font=SCOREBOARD_FONT)
		self.goto(x=35, y=self.y_position)
		self.write(f"{self.player_right_score}", align="left", font=SCOREBOARD_FONT)

	def rreset(self):
		self.player_left_score = 0
		self.player_right_score = 0

	def refresh(self):
		self.clear()
		self.goto(x=-35, y=self.y_position)
		self.write(f"{self.player_left_score}", align="right", font=SCOREBOARD_FONT)
		self.goto(x=35, y=self.y_position)
		self.write(f"{self.player_right_score}", align="left", font=SCOREBOARD_FONT)

	def player_left_point(self):
		self.player_left_score += 1
		self.refresh()

	def player_right_point(self):
		self.player_right_score += 1
		self.refresh()
