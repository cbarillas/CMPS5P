# Carlos Barillas
# cbarilla@ucsc.edu
# Programming Assignment 2
# This program uses the turtle module to draw an n pointed star, where n is any odd integer greater than or equal to 3 to be obtained from user input

import turtle

n = int(input("Enter an odd integer greater than or equal to 3: "))
wn = turtle.Screen()
wn.title(str(n)+"-pointed star")               #title of window

myTurtle = turtle.Turtle()
myTurtle.color("blue" , "green")               #color of pen, fill color
myTurtle.pensize(2)                            #width of pen

myTurtle.ht()                                  #hides turtle 

myTurtle.begin_fill()

myTurtle.backward(150)
myTurtle.forward(300)                          #number of pixels it moves forward

for i in range(n):
    myTurtle.dot(10, "red")                    #diameter of dot, color of dot
    myTurtle.right(180 - (180/n))
    myTurtle.forward(300)

myTurtle.end_fill()

wn.mainloop()                                                                              
