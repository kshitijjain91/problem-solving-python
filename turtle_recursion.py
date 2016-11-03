import turtle
from turtle import Turtle, Screen 

my_turtle = Turtle()
my_win = Screen()

def draw_spiral(my_turtle, line_len):
	if line_len > 0:
		my_turtle.forward(line_len)
		my_turtle.right(90)
		draw_spiral(my_turtle, line_len - 5)

draw_spiral(my_turtle, line_len = 100)
my_win.exitonclick()


