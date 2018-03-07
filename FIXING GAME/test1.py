import turtle
from turtle import Turtle
import keyboard
PRESSED = False
class ladder(Turtle):
	def __init__(self):
		Turtle.__init__(self)

		self.pu()
		self.shape("square")
		self.shapesize(20)		
		#self.ladder_length=self.shapesize()
		#def create_ladder(character_current_y,character_current_x):
			#for i in range(x):
if keyboard.is_pressed('space'):
	PRESSED=True
	x=character.xcor()+20
	y=character.ycor()
	ladder.goto(x,y)
	ladder.stamp()
	while PRESSED==True:

		ladder.goto(x,y+20)
		ladder.stamp()
		if keyboard.is_pressed('space'):
			PRESSED=False

#def move():
#	global PRESSED
#	PRESSED = not PRESSED


# while(PRESSED):
# 	print("The key was pressed. Press agin to stop.")
# turtle.onkey(move, 'space')

# turtle.listen()

turtle.mainloop()


