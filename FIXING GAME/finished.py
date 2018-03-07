import turtle
import time
from turtle import *
#import keyboard
#character=turtle.clone()
#character.shape("circle")
turtle.register_shape('ladderf.gif')
global direction
global current_x
global last_x
stamp_pos=[]

class Platform(Turtle):
	def __init__(self,x,y):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.shapesize(1,5)
		self.color("black")
		self.shape("square")


character = turtle.clone()
character.shape("circle")
character.shapesize(1,)
character.penup()
character.setpos(0,-140)
turtle.hideturtle()
UP = 0 
LEFT = 1
DOWN = 2
RIGHT = 3
direction= UP
start_pos = character.pos()
def move_char():
	my_pos = character.pos()
	x_pos = my_pos[0]
	y_pos = my_pos[1]

	if direction==RIGHT: #and character.xcor()==main_ladder.xcor() and character.ycor()==start_pos[1]:
		character.forward(20)
	if direction==LEFT: #and character.xcor()==main_ladder.xcor() and character.ycor()==start_pos[1]:

		character.backward(20)
	if direction==UP:
		character.setheading(90)
		character.forward(20)
		character.setheading(0)
def left():
	
	direction = LEFT
	
	current_x=character.xcor()
	last_x=current_x+1
	move_char()
def right():

	direction = RIGHT
	current_x=character.xcor()
	last_x=current_x-1
	move_char()
def up():

	direction= UP
	if(character.xcor()==main_ladder.xcor()):
		move_char()

Platform1=Platform(0,0)
Platform2=Platform(60,140)


class Ladder(Turtle):
	def __init__(self):
		Turtle.__init__(self)

		self.pu()
		self.shape("square")
		self.shapesize(1)
		self.shape('ladderf.gif')
		self.speed(1)	
		#self.ladder_length=self.shapesize()
		#def create_ladder(character_current_y,character_current_x):
			#for i in range(x):
	# if keyboard.is_pressed('space'):
	# 	PRESSED=True
	# 	x=character.xcor()+20
	# 	y=character.ycor()
	# 	self.goto(x,y)
	# 	self.stamp()
	# 	while PRESSED==True:

	# 		self.goto(x,y+20)
	# 		self.stamp()
	# 		if keyboard.is_pressed('space'):
	# 			PRESSED=False

main_ladder=Ladder()
main_ladder.ht()

def create_ladder():

	
	global PRESSED
	PRESSED=True
	x=character.xcor()
	y=character.ycor()

	if current_x-last_x<0:
		main_ladder.goto(x-20,y)
	else:
		main_ladder.goto(x+20,y)	
	main_ladder.stamp()


	while PRESSED==True:
		time.sleep(0.1)
		if current_x-last_x<0:
			main_ladder.goto(x-20,y+20)	
		else:
			main_ladder.goto(x+20,y+20)


		y+=20
		main_ladder.stamp()



def stop_building():
	global PRESSED
	PRESSED=False

turtle.onkey(create_ladder, 'space')

turtle.onkey(stop_building, 's')

turtle.onkey(left,"a")
turtle.onkey(right,"d")
turtle.onkey(up,"w")



turtle.listen()
turtle.getscreen().update()

# turtle.listen()

turtle.mainloop()


