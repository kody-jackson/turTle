import turtle


screen = turtle.Screen()
screen.screensize(canvwidth= 500, canvheight= 500)
screen.bgcolor('tan')
t = turtle.Turtle()

#moves turtle around screen
t.penup()
t.goto(80,15)
t.pendown()




t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor('blue')
t.pensize(3)
#t.setheading(90)
t.circle(35)
t.penup()
t.goto(0,15)
t.pendown()
t.pencolor('black')
t.pensize(3)
#t.setheading(90)
t.circle(35)
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor('red')
t.pensize(3)
#t.setheading(90)
t.circle(35)
t.penup()
t.goto(-40,-20)
t.pendown()
t.pencolor('yellow')
t.pensize(3)
#t.setheading(90)
t.circle(35)
t.penup()
t.goto(40,-20)
t.pendown()
t.pencolor('green')
t.pensize(3)
#t.setheading(90)
t.circle(35)

t.pencolor('purple')
t.penup()
t.goto(0,100)
t.pendown()

t.write("Winter Olympics",font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()

t.write("2026",font=("Arial",30,"bold italic"),align="center")



















turtle.done()