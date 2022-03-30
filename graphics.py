from turtle import Turtle


class Graphics(Turtle):
	def __init__(self, imp_width, imp_height):
		super().__init__()
		self.screen_width = imp_width
		self.screen_height = imp_height
		self.playground_upleft = (-(self.screen_width // 2) + 20, self.screen_height // 2 - 20)
		self.playground_dnleft = (-(self.screen_width // 2) + 20, -(self.screen_height // 2) + 28)
		self.playground_upright = (self.screen_width // 2 - 28, self.screen_height // 2 - 20)
		self.playground_dnright = (self.screen_width // 2 - 28, -(self.screen_height // 2) + 28)
		self.hideturtle()
		self.color("white")
		self.penup()
		self.speed("fastest")

	def get_borders(self):
		return self.playground_dnleft[0], self.playground_dnright[0], self.playground_upleft[1], self.playground_dnleft[1]

	def prepare_game_start(self):
		self.draw_border()
		self.draw_net()

	def draw_border(self):
		self.goto(self.playground_upleft)
		self.pendown()
		self.goto(self.playground_dnleft)
		self.goto(self.playground_dnright)
		self.goto(self.playground_upright)
		self.goto(self.playground_upleft)
		self.penup()

	def draw_net(self):
		self.goto(x=0, y=self.playground_upleft[1])
		self.setheading(270)
		while self.ycor() >= self.playground_dnleft[1] + 5:
			self.pendown()
			self.forward(10)
			self.penup()
			self.forward(10)
