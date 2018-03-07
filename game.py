
import turtle 
from Gproject import Platform
from char import character
from char import *

UP = 0 
LEFT = 1
DOWN = 2
RIGHT = 3

direction= UP

Platform1= Platform(0,0)


character = character()

turtle.onkeypress(left,"a")
turtle.onkeypress(right,"d")
turtle.onkeypress(up,"w")

turtle.listen()


turtle.exitonclick()
character.mainloop()
Platform1.mainloop()
turtle.mainloop()