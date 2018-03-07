import turtle


##################left##################
#to create new turtle onkey press move 
left_arrow = "a"
right_arrow = "d"
up_arrow = "w"
def left():
	character.backward(-20)
	onkeypress(left_arrow,left())
def right():
	character.forward(20)
	onkeypress(right_arrow,right())
def up():
	character.upward(40)
	onkeypress(up_arrow,up())


turtle.mainloop()




