import turtle
t=turtle.Turtle()
m=turtle.Screen()
t.speed(20)
m.bgcolor("light blue")

t.pu()
t.goto(-840,-100)
t.pd()
t.pensize(4)
t.color("green")

t.color("green","blue")
t.begin_fill()
for i in range(4):
    t.fd(1280)
    t.rt(90)


t.end_fill()

m=turtle.Turtle()

print("\n")
print("Drawing Sun")
m.pensize(2)
m.pu()
m.goto(-190,200)
m.pd()
m.color("orange")
for i in range(12):
    m.fd(70)
    m.backward(70)
    m.lt(360/12)
m.pu()
m.goto(-190,150)
m.pd()
m.color("red","yellow")
m.begin_fill()
m.circle(50)
m.end_fill()
m.hideturtle()

rainbowColors = ["#FF0000","#FFA600","#FFFF00","#62FF00","#1E56FC","#4B00FF","#CC00FF","69C5FF"]
size=150

t.penup()
t.goto(50,-90)
t.pd()

for color in rainbowColors:
	t.color(color)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(size)
	t.end_fill()
	size -= 20
