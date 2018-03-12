
import random
import turtle
from turtle import*

shape ("turtle")
pensize(40)
pencolor("yellow"),circle(70,360)



def tree(size, myTurtle):
    myTurtle.pensize(size / 10)

    if size < random.randint(1,2) * 20:
        myTurtle.color("green")
    else:
        myTurtle.color("brown")

    if size > 5:
        myTurtle.forward(size)
        myTurtle.left(25)
        tree(size - random.randint(10, 20), myTurtle)
        myTurtle.right(50)
        tree(size - random.randint(10, 20), myTurtle)
        myTurtle.left(25)
        myTurtle.penup()
        myTurtle.backward(size)
        myTurtle.pendown()


window = turtle.Screen()
window.bgcolor ("orange")

myTurtle = turtle.Turtle()
myTurtle.color("brown", "blue")
myTurtle.left(90)
myTurtle.speed(0)
myTurtle.penup()
myTurtle.setpos(0, -230)
myTurtle.pendown()

tree(120, myTurtle)
myTurtle.penup()
myTurtle.pensize(25)
myTurtle.goto(-490,-260)
myTurtle.color("bLUE")
myTurtle.write("The best friend of earth of man is the tree.Lets go green to get our globe clean.",font=("Arial", 19, "normal"))
myTurtle.goto(440,-290)
myTurtle.write("REETHU & RAMYA - ECE",font=("Arial", 13, "normal"))
input()


