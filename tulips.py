import turtle
from random import *
sky=turtle.Turtle()
sky.color('#e5e5ff')
sky.pensize(100)
sky.speed(3)
sky.penup()
sky.goto(-320,-150)
sky.pendown()

skycol = ['add8e6','b5d8e5','bdd8e4','c5d8e3','cdd8e3','d6d8e2','ded8e1','e6d8e1','eed8e0','f6d8df','ffd9df']

def drawsky():
    print("Drawing sky")
    for i in skycol:
        temp = '#' + i
        sky.color(temp)
        sky.forward(620)
        sky.left(90)
        sky.forward(20)
        sky.left(90)

        sky.color(temp)
        sky.forward(620)
        sky.right(90)
        sky.forward(20)
        sky.right(90)

drawsky()


cloud=turtle.Turtle()
def clouddraw():
    print("\n")
    cloud.color('white')
    
    def randloc():
        location = randint(-250,250),randint(0,100)
        return location
    
    def brushstroke(randloc,leng):
        cloud.penup()
        cloud.goto(randloc)
        cloud.pendown()
        cloud.pensize(randint(3,5))
        cloud.forward(leng)
        
    def singlecloud():
        temp = randloc()
        temp2 = temp[1]
        temp3 = temp[0]
        leng = 30
            
        for i in range(20):
            temp4 = (temp3, temp2)
            brushstroke(temp4,leng)
            temp2 += 1
            temp3 += randint(-10,10)
            leng += randint(-40,40)

    for i in range(4):
        print("Drawing cloud:",i+1)
            
        singlecloud()
clouddraw()

        

m= turtle.Turtle()
m.pensize(10)
m.color('#a9a9a9')
m.speed(3)

m.penup()
m.goto(-340,-100)
m.pendown()
m.begin_fill()
print("\n")
print("Drawing mountain 1")
for i in range(9):
    templen = randint(20,200)
    
    tempang = randint(45,80)
    
    m.left(tempang)
    m.forward(templen)
    m.right(2*tempang)
    m.forward(templen)
    m.setheading(0)
    
m.goto(300,-400)
m.goto(-340,-400)
m.end_fill()


m.color('#556b2f')
m.penup()
m.goto(-340,-150)
m.pendown()
m.begin_fill()
print("Drawing mountain 2")
for i in range(7):
    templen = randint(20,200)
    
    tempang = randint(20,30)
    
    m.left(tempang)
    m.forward(templen)
    m.right(2*tempang)
    m.forward(templen)
    m.setheading(0)
    
m.goto(300,-400)
m.goto(-340,-400)
m.end_fill()


m.color('#8a360f')
m.penup()
m.goto(-340,-175)
m.pendown()
m.begin_fill()
print("Drawing mountain 3")
for i in range(7):
    templen = randint(20,200)
    
    tempang = randint(10,20)
    
    m.left(tempang)
    m.forward(templen)
    m.right(2*tempang)
    m.forward(templen)
    m.setheading(0)
    
m.goto(300,-400)
m.goto(-340,-400)
m.end_fill()

print("\n")
print("Drawing Sun")
m.pensize(7)
m.pu()
m.goto(0,200)
m.pd()
m.color("orange")
for i in range(12):
    m.fd(70)
    m.backward(70)
    m.lt(360/12)
    
m.pu()
m.goto(0,150)
m.pd()
m.color("red",'#ffc125')
m.begin_fill()
m.circle(50)
m.end_fill()
m.hideturtle()

