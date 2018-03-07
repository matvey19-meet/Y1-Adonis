import turtle

from turtle import Turtle

UP = 0 
LEFT = 1
DOWN = 2
RIGHT = 3
direction = 0
def left():
	global direction
	direction = LEFT

def right():
	global direction
	direction = RIGHT

def up():
	global direction
	direction = UP


class character(Turtle):
	def __init__(self):
		self = turtle.clone()
		self.shape("circle")
		self.penup()
		self.setpos(0,-145)
		
		direction= UP

	def move_char(self):
		my_pos = self.pos()
		x_pos = my_pos[0]
		y_pos = my_pos[1]

		if direction==RIGHT:
			self.forward(20)
		if direction==LEFT:
			self.backward(20)
		if direction==UP:
			self.setheading(90)
			self.forward(20)
			self.setheading(0)
	
	turtle.onkeypress(left,"a")
	turtle.onkeypress(right,"d")
	turtle.onkeypress(up,"w")

	turtle.listen()



character= character()

while(1):
	character.move_char()
turtle.mainloop()