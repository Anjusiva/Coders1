

import turtle
import math

# Set the background color
screen = turtle.Screen()
screen.bgcolor("darkblue")

# Create our turtle
eee = turtle.Turtle()



# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
# Define a function to draw and fill an equalateral right 
# triangle with the given hypotenuse length and color.  This
# is used to create a roof shape.
def drawTriangle(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()
  
# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
# Define a function to draw four sun rays of the given length,
# for the sun of the given radius.  The turtle starts in the 
# center of the circle.
def drawFourRays(t, length, radius):
  for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + radius)
    t.left(90)

# Draw and fill the front of the house
eee.penup() 
eee.goto(-150, -120)
eee.pendown()
drawRectangle(eee, 100, 110, "blue")

# Draw and fill the front door
eee.penup()
eee.goto(-120, -120)
eee.pendown()
drawRectangle(eee, 40, 60, "lightgreen")

# Front roof
eee.penup()
eee.goto(-150, -10)
eee.pendown()
drawTriangle(eee, 100, "magenta")

# Side of the house
eee.penup()
eee.goto(-50, -120)
eee.pendown()
drawParallelogram(eee, 60, 110, "yellow")

# Window
eee.penup()
eee.goto(-30, -60)
eee.pendown()
drawParallelogram(eee, 20, 30, "brown")

# Side roof
eee.penup()
eee.goto(-50, -10)
eee.pendown()
eee.fillcolor("orange")
eee.begin_fill()
eee.left(30)
eee.forward(60)
eee.left(105)
eee.forward(100 / math.sqrt(2))
eee.left(75)
eee.forward(60)
eee.left(105)
eee.forward(100 / math.sqrt(2))
eee.left(45)
eee.end_fill()

# Tree base
eee.penup() 
eee.goto(100, -130)
eee.pendown()
drawRectangle(eee, 20, 40, "brown")

# Tree top
eee.penup() 
eee.goto(65, -90)
eee.pendown()
drawTriangle(eee, 90, "lightgreen")
eee.penup() 
eee.goto(70, -45)
eee.pendown()
drawTriangle(eee, 80, "lightgreen")
eee.penup() 
eee.goto(75, -5)
eee.pendown()
drawTriangle(eee, 70, "lightgreen")

# moon
eee.penup() 
eee.goto(55, 110)
eee.fillcolor("white")
eee.pendown()
eee.begin_fill()
eee.circle(24)
eee.end_fill()
 # birds
eee.pensize(10)
eee.rt(135)
eee.fd(20)
eee.lf(135)
eee.fd(20)
#star
STAR_SIZE = 500

EXPANSION = 1.2
TRANSLATION = STAR_SIZE * EXPANSION / 4

eee.hideturtle()
eee.color("purple")
eee.shape("triangle")
eee.turtlesize(STAR_SIZE * EXPANSION / 20)

for _ in range(5):
    eee.right(72)
    eee.forward(TRANSLATION)
    eee.stamp()
    eee.backward(TRANSLATION)



# Sun ray
#eee.penup()
#eee.goto(55, 134)
#eee.pendown()
#drawFourRays(eee, 25, 24)
#eee.right(45)
#drawFourRays(eee, 15, 24)
#eee.left(45)

# Put down some labels
eee.color("black")
eee.penup()
eee.goto(-150, 70)
eee.pendown()
eee.write("House", None, None, "14pt bold")
eee.penup()
eee.goto(150, -150)
eee.pendown()
eee.write("Tree", None, None, "14pt bold")
eee.penup()
eee.goto(130, 150)
eee.pendown()
eee.write("Sun", None, None, "14pt bold")

# Bring the turtle down to the front door, and we're done!
eee.penup()
eee.goto(-100, -150)
eee.left(90)




