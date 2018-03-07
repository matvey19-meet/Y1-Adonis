
from turtle import Turtle
import turtle 
import random



class Platform(Turtle):
	def __init__(self,x,y):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.shapesize(2,8)
		self.color("black")
		self.shape("square")



turtle.mainloop()
