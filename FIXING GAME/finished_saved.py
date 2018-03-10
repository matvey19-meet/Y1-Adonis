import turtle
import time

from turtle import *


turtle.register_shape('char.gif')
turtle.register_shape('ladderf.gif')
turtle.register_shape('plat.gif')

stamp_pos=[]
char_pos=[]
plat_pos=[]

ground_lvl= -140
#CREATING CHARACTER
character = turtle.clone()
character.shape("circle")
character.penup()
character.setpos(0,ground_lvl)
start_pos = character.pos()
char_pos.append(start_pos)
turtle.hideturtle()

#CLASSES
class Platform(Turtle):
	def __init__(self,x,y):
		Turtle.__init__(self)
		self.shape("plat.gif")
		self.penup()
		self.goto(x, y)
		
class Ladder(Turtle):
	def __init__(self):
		Turtle.__init__(self)
		self.pu()
		self.shape("square")
		self.shapesize(1)

#DEFINING THE MOVEMENT OF THE CHARACTER
def move_char():
	my_pos = character.pos()

	x_pos = my_pos[0]
	y_pos = my_pos[1]

	if direction==RIGHT:
		character.forward(20)
		char_pos.append(character.pos())
	if direction==LEFT:
		character.backward(20)
		char_pos.append(character.pos())
	if direction==UP:
		character.setheading(90)
		character.forward(20)
		character.setheading(0)
		print("moved")
		char_pos.append(character.pos())
def left():
	global direction
	direction = LEFT
	global current_x
	global last_x
	current_x=character.xcor()
	last_x=current_x+1
	if char_pos[-1] not in stamp_pos[1:-2]:
		move_char()
def right():

	global direction
	direction = RIGHT
	global current_x
	global last_x
	current_x=character.xcor()
	last_x=current_x-1
	if char_pos[-1] not in stamp_pos[1:-2]:
		move_char()
def up():
	if char_pos[-1] in stamp_pos[0:-1]:
		global direction
		direction= UP
		move_char()


#DEFINING FUNCTION FOR THE LADDER
def create_ladder():

	global direction
	global PRESSED
	PRESSED=True
	x=character.xcor()
	y=character.ycor()

	if direction==LEFT:
		main_ladder.goto(x-20,y)
		stamp_pos.append(main_ladder.pos())
	else:
		main_ladder.goto(x+20,y)
		stamp_pos.append(main_ladder.pos())

	
	main_ladder.stamp()


	while PRESSED==True:
		time.sleep(0.1)
		if direction==LEFT:
			main_ladder.goto(x-20,y+20)

		else:
			main_ladder.goto(x+20,y+20)


		y+=20
		main_ladder.stamp()
		stamp_pos.append(main_ladder.pos())
def stop_building():
	global PRESSED
	PRESSED=False

Platform1=Platform(0,0)
Platform2=Platform(60,140)

UP = 0 
LEFT = 1
DOWN = 2
RIGHT = 3
direction= UP



main_ladder=Ladder()
main_ladder.shape("ladderf.gif")
main_ladder.ht()
main_ladder.speed(1)



turtle.onkey(create_ladder, 'space')
turtle.onkey(stop_building, 's')

turtle.onkey(left,"a")
turtle.onkey(right,"d")
turtle.onkey(up,"w")

turtle.listen()

turtle.getscreen().update()

# turtle.listen()

turtle.mainloop()


