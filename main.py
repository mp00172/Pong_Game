from turtle import Screen
from graphics import Graphics
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import random
from config import *
import time
from tkinter import messagebox

screen = Screen()
screen.tracer(0)


def screen_setup(imp_width, imp_height):
	screen.setup(width=imp_width, height=imp_height)
	screen.bgcolor("black")
	screen.title("Pong")


screen_setup(imp_width=SCREEN_WIDTH, imp_height=SCREEN_HEIGHT)

graphics = Graphics(imp_width=SCREEN_WIDTH, imp_height=SCREEN_HEIGHT)
playground_x_left, playground_x_right, playground_y_up, playground_y_dn = graphics.get_borders()
graphics.prepare_game_start()

scoreboard = Scoreboard(imp_height=SCREEN_HEIGHT)

paddle_left = Paddle(x_position=(playground_x_left + PADDLE_X_OFFSET), y_up_limit=playground_y_up,
					 y_dn_limit=playground_y_dn)
paddle_right = Paddle(x_position=(playground_x_right - PADDLE_X_OFFSET), y_up_limit=playground_y_up,
					  y_dn_limit=playground_y_dn)


def paddle_bounce_flat():
	if ball.xcor() >= playground_x_right - BALL_OFF_PADDLE or ball.xcor() <= playground_x_left + BALL_OFF_PADDLE:
		if ball.distance(paddle_right) < 40 or ball.distance(paddle_left) < 40:
			return True
	return False


def paddle_bounce_angle():
	if ball.xcor() >= playground_x_right - BALL_OFF_PADDLE or ball.xcor() <= playground_x_left + BALL_OFF_PADDLE:
		if 40 <= ball.distance(paddle_right) <= 50 or 40 <= ball.distance(paddle_right) <= 50 or 40 <= ball.distance(
				paddle_left) <= 50 or 40 <= ball.distance(paddle_left) <= 50:
			return True
	return False


def make_angle_bounce():
	if 90 < ball.heading() < 270:
		if ball.ycor() > paddle_left.ycor():
			ball.setheading(ball.heading() - 180 - 2 * (ball.heading()))
			ball.left(20)
		elif ball.ycor() < paddle_left.ycor():
			ball.setheading(ball.heading() - 180 - 2 * (ball.heading()))
			ball.right(20)
	elif 0 < ball.heading() < 90 or 270 < ball.heading() < 360:
		if ball.ycor() > paddle_right.ycor():
			ball.setheading(ball.heading() - 180 - 2 * (ball.heading()))
			ball.right(20)
		elif ball.ycor() < paddle_right.ycor():
			ball.setheading(ball.heading() - 180 - 2 * (ball.heading()))
			ball.left(20)


messagebox.showinfo(title="Pong", message="Welcome to Pong Game!\n"
										  "\n"
										  "Use UP and DOWN arrow keys to move paddle on the right.\n"
										  "Computer will play with the left paddle.\n"
										  "\n"
										  "Press ENTER to start!")

screen.listen()

screen.onkey(key=LEFT_PADDLE_UP_KEY, fun=paddle_left.move_up)
screen.onkey(key=LEFT_PADDLE_DN_KEY, fun=paddle_left.move_down)
screen.onkey(key=RIGHT_PADDLE_UP_KEY, fun=paddle_right.move_up)
screen.onkey(key=RIGHT_PADDLE_DN_KEY, fun=paddle_right.move_down)

program_running = True
ball = Ball(playground_x_left, playground_x_right, playground_y_up, playground_y_dn)

while program_running:

	match_running = True
	match_winner = None

	eval(random.choice(serve_options))

	while match_running:

		ball.move()
		paddle_left.comp_paddle_move(ball.get_position())

		if paddle_bounce_flat():
			ball.setheading(ball.heading() - 180 - 2 * (ball.heading()))
		elif paddle_bounce_angle():
			make_angle_bounce()
		if ball.check_point_winner() == "left":
			scoreboard.player_left_point()
			time.sleep(PAUSE_BEFORE_SERVE_IN_SECS)
			ball.serve_to_right()
		elif ball.check_point_winner() == "right":
			scoreboard.player_right_point()
			time.sleep(PAUSE_BEFORE_SERVE_IN_SECS)
			ball.serve_to_left()
		time.sleep(0.01)
		screen.update()

		if scoreboard.player_left_score == 0:
			if scoreboard.player_right_score == SCORE_DROPOUT:
				match_running = False
				match_winner = "player"
		elif scoreboard.player_right_score == 0:
			if scoreboard.player_left_score == SCORE_DROPOUT:
				match_running = False
				match_winner = "comp"
		elif scoreboard.player_left_score == SCORE_FINAL:
			match_running = False
			match_winner = "comp"
		elif scoreboard.player_right_score == SCORE_FINAL:
			match_running = False
			match_winner = "player"

	if match_winner == "player":
		another_game = messagebox.askyesno(title="Pong", message="You win!\n"
																 "\n"
																 "Play again?")

	else:
		another_game = messagebox.askyesno(title="Pong", message="You lose.\n"
																 "\n"
																 "Play again?")
	if not another_game:
		messagebox.showinfo(title="Pong", message="Thank you for playing!\n"
												  "\n"
												  "Bye!")
		program_running = False
	else:
		scoreboard.rreset()
		scoreboard.refresh()

screen.bye()
