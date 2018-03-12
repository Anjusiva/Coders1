import turtle
turtle.bgcolor("black")
color = ["red","green","white","blue","orange","purple","pink","yellow","brown","skyblue"] # Make a list of colors to picvk from.
turtle.setup(500,400)    #choosing the screen size

# to create the ocean
# rightside
t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(0)

t1.begin_fill()
t1.color("blue")
for i in range(4):
    t1.fd(700)
    t1.right(90)
t1.end_fill()
t1.goto(0,0)
t1.fd(700)
#leftside
t2 = turtle.Turtle()
t2.shape("turtle")
t2.speed(0)

t2.begin_fill()
t2.color("blue")
for i in range(4):
    t2.bk(700)
    t2.left(90)
t2.end_fill()

# to create an island in rightside


##################
#land

t2.forward(200)
t2.right(90)
t2.fd(280)
t2.left(90)
t2.fd(200)
t2.color("brown")
t2.shape("circle")
t2.shapesize(26,43,35)
t2.fillcolor("green")

########################### 2
##tree1
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(650,-200)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(650,-205)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()

##tree2
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(620,-155)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(620,-160)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()

##tree3
te=turtle.Turtle()
te.color("blue")
te.bk(40)
te.right(90)
te.fd(200)
te.left(90)
te.fd(15)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(590,-135)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()
#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(590,-140)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()



##tree4
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(520,-105)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()
#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(520,-110)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()




##tree5
te=turtle.Turtle()
te.color("blue")
te.bk(40)
te.right(90)
te.fd(200)
te.left(90)
te.fd(15)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(570,-155)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(40)
te.right(90)
te.fd(200)
te.left(90)
te.fd(15)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(570,-160)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()


##tree6
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(540,-220)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(540,-225)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()




##tree7
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(485,-150)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(485,-155)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()




######################## 1
##tree1
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(440,-75)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(440,-80)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()

##tree2
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(340,-55)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(340,-60)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()


##tree3
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(250,-110)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(250,-115)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()

##############################
###house
#house 1

wn=turtle.Screen()
td=turtle.Turtle()

td.color("blue")

td.forward(200)
td.right(90)
td.fd(37)
td.color("brown")
td.fd(36)
td.color("green")
td.fd(110)
td.left(90)
td.fd(250)
#for triangle



td.begin_fill()
td.color("purple")
td.backward(40)
td.left(30)
td.forward(45)
td.right(60)
td.forward(45)
td.left(30)
td.backward(45)
td.end_fill()

#for square and door
td.begin_fill()
td.color("orange")
td.forward(30)
td.right(90)
td.forward(45)
td.right(90)

td.forward(30)
td.left(90)
td.backward(25)
td.left(90)
td.forward(25)
td.right(90)
td.forward(25)


td.left(90)
td.backward(45)
td.left(90)
td.forward(45)
td.end_fill()    


#house 2

wn=turtle.Screen()
td=turtle.Turtle()
td.color("blue")

td.forward(150)
td.right(90)
td.fd(60)
td.color("brown")
td.fd(30)
td.color("green")
td.fd(160)
td.left(90)
td.fd(250)
#for triangle



td.begin_fill()
td.color("purple")
td.backward(40)
td.left(30)
td.forward(45)
td.right(60)
td.forward(45)
td.left(30)
td.backward(45)
td.end_fill()

#for square and door
td.begin_fill()
td.color("orange")
td.forward(30)
td.right(90)
td.forward(45)
td.right(90)

td.forward(30)
td.left(90)
td.backward(25)
td.left(90)
td.forward(25)
td.right(90)
td.forward(25)


td.left(90)
td.backward(45)
td.left(90)
td.forward(45)
td.end_fill()    



#house 3

wn=turtle.Screen()
td=turtle.Turtle()
td.color("blue")

td.forward(100)
td.right(90)
td.fd(80)
td.color("brown")
td.fd(45)
td.color("green")
td.fd(50)
td.left(90)
td.fd(250)
#for triangle

td.begin_fill()
td.color("purple")
td.backward(40)
td.left(30)
td.forward(45)
td.right(60)
td.forward(45)
td.left(30)
td.backward(45)
td.end_fill()

#for square and door
td.begin_fill()
td.color("orange")
td.forward(30)
td.right(90)
td.forward(45)
td.right(90)

td.forward(30)
td.left(90)
td.backward(25)
td.left(90)
td.forward(25)
td.right(90)
td.forward(25)


td.left(90)
td.backward(45)
td.left(90)
td.forward(45)
td.end_fill()    




#house 4

wn=turtle.Screen()
td=turtle.Turtle()
td.color("blue")

td.forward(20)
td.right(90)
td.fd(140)
td.color("brown")
td.fd(45)
td.color("green")
td.left(90)
td.fd(200)
#for triangle

td.begin_fill()
td.color("purple")
td.backward(40)
td.left(30)
td.forward(45)
td.right(60)
td.forward(45)
td.left(30)
td.backward(45)
td.end_fill()

#for square and door
td.begin_fill()
td.color("orange")
td.forward(30)
td.right(90)
td.forward(45)
td.right(90)

td.forward(30)
td.left(90)
td.backward(25)
td.left(90)
td.forward(25)
td.right(90)
td.forward(25)


td.left(90)
td.backward(45)
td.left(90)
td.forward(45)
td.end_fill()    




#house 5

wn=turtle.Screen()
td=turtle.Turtle()
td.color("blue")

td.forward(50)
td.right(90)
td.fd(110)
td.color("brown")
td.fd(50)
td.color("green")
td.fd(80)
td.left(90)
td.fd(250)

#for triangle
td.begin_fill()
td.color("purple")
td.backward(40)
td.left(30)
td.forward(45)
td.right(60)
td.forward(45)
td.left(30)
td.backward(45)
td.end_fill()

#for square and door
td.begin_fill()
td.color("orange")
td.forward(30)
td.right(90)
td.forward(45)
td.right(90)

td.forward(30)
td.left(90)
td.backward(25)
td.left(90)
td.forward(25)
td.right(90)
td.forward(25)


td.left(90)
td.backward(45)
td.left(90)
td.forward(45)
td.end_fill()

########################## 3
##tree1
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(170,-155)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(170,-155)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()



##tree2
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(130,-95)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(130,-100)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()




##tree3
te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(85,-120)
te.begin_fill()
te.color("seagreen")
te.circle(20)
te.end_fill()

#trunk

te=turtle.Turtle()
te.color("blue")
te.bk(10)
te.right(90)
te.fd(140)
te.left(90)
te.fd(30)
te.color("brown")
te.fd(40)
te.color("green")
te.fd(50)

te.goto(85,-125)
te.begin_fill()
te.color("brown")
te.bk(5)
te.left(90)
te.bk(50)
te.left(90)
te.bk(10)
te.left(90)
te.bk(50)
te.left(90)
te.end_fill()

############################ 4
##tree1




#############################
##moon
turtle.bgcolor("black")
color=["white","ivory","blue"]
t=turtle.Turtle()
t.goto(50,170)
t.backward(200)
t.begin_fill()
t.color("ivory")
t.circle(50)
t.left(90)
t.fd(20)
t.end_fill()


##############################
##star1
s = turtle.Turtle()
s.goto(70,180)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star2
s = turtle.Turtle()
s.goto(-400,200)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star3
s = turtle.Turtle()
s.goto(-120,80)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star4
s = turtle.Turtle()
s.goto(-10,160)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##strar5
s = turtle.Turtle()
s.goto(-300,200)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star6
s = turtle.Turtle()
s.goto(-620,180)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star7
s = turtle.Turtle()
s.goto(-10,250)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star8
s = turtle.Turtle()
s.goto(200,200)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star9
s = turtle.Turtle()
s.goto(650,160)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##strar10
s = turtle.Turtle()
s.goto(400,250)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()


##strar11
s = turtle.Turtle()
s.goto(350,75)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()

##star12
s = turtle.Turtle()
s.goto(-500,260)
s.color("yellow")
s.begin_fill()
for i in range(5):
    s.forward(20)
    s.right(144)
s.fd(10)
s.right(90)
s.fd(10)
#s.done()
s.end_fill()



#############################
##boat
t=turtle.Turtle()
t.color("blue")
t.bk(500)
t.right(90)
t.fd(180)
t.left(90)

t.begin_fill()
t.color("purple")
t.fd(100)
t.left(60)
t.fd(25)
t.left(120)
t.fd(135)
t.left(130)
t.fd(30)
t.left(70)
t.fd(15)
t.end_fill()

t=turtle.Turtle()
t.color("black")
t.bk(450)
t.right(90)
t.color("blue")
t.fd(77)
t.begin_fill()
t.color("yellow")
t.fd(80)
t.right(100)
t.fd(90)
t.right(130)
t.fd(120)
t.end_fill()




