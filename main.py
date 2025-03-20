import turtle
import random
screen = turtle.Screen()
screen.screensize(canvwidth= 500, canvheight= 500)
screen.bgcolor('black')
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(0,200)
t.pencolor("white")
t.pendown()
t.write("Backround Color",font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(-75,100)
t.pencolor("tan")
t.pendown()
t.write("1. Tan",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,50)
t.pencolor("azure")
t.pendown()
t.write("2. Azure",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,0)
t.pencolor("aquamarine")
t.pendown()
t.write("3. AquaMarine",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,-50)
t.pencolor("darkkhaki")
t.pendown()
t.write("4. DarkKhaki",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(0,-150)
t.pencolor("blue")
t.pendown()
t.write("Choose one",font=("Arial",30,"bold italic"),align="center")

choose = int(input('Choose one: '))
if choose ==1:
    screen.bgcolor('tan')
elif choose ==2:
    screen.bgcolor('azure')
elif choose ==3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('darkkhaki')
t.clear()

t.penup()
t.goto(0,0)
t.pencolor("black")
t.pendown()
t.write("Enter Your Name",font=("Arial",30,"bold italic"),align="center")

name = input("Enter your name: ")
t.clear()

#number1 = int(input("Enter a number: "))
#number2 = int(input("Enter a second number: "))
operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    number1 = random.randint(-100,100)
    number2 = random.randint(-100,100)
    solution = number1 + number2

elif operation == 2:
    symbol = "-"
    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)
    solution = number1 - number2

elif operation == 3:
    symbol = "*"
    number1 = random.randint(-10, 10)
    number2 = random.randint(-10, 10)
    solution = number1 * number2

elif operation == 4:
    symbol = "/"
    number1 = random.randint(-10, 10)
    number2 = random.randint(1, 10)
    sign = random.randint(1,2)
    if sign == 2:
        number2 = -1 * number2
    solution = number1 / number2

t.penup()
t.goto(0,100)
t.pencolor("blue")
t.pendown()
t.write(name,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(-200,0)
t.pencolor("red")
t.pendown()
t.write(number1,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(-100,0)
t.pencolor("black")
t.pendown()
t.write(symbol,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(0,0)
t.pencolor("yellow")
t.pendown()
t.write(number2,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(100,0)
t.pencolor("black")
t.pendown()
t.write("=",font=("Arial",30,"bold italic"),align="center")

answer = float(input("Enter answer: "))


t.penup()
t.goto(200,0)
t.pencolor("purple")
t.pendown()
t.write(solution,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pencolor("black")
t.pendown()
t.write("your answer is : "+str(answer),font=("Arial",30,"bold italic"),align="center")

if solution == answer:
    screen.bgcolor('dodgerblue')
    t.penup()
    t.goto(0,50)
    t.pencolor("black")
    t.pendown()
    t.write("Correct ", font=("Arial",30,"bold italic"),align="center")
else:
    screen.bgcolor('darkorange')
    t.penup()
    t.goto(0,50)
    t.pencolor("black")
    t.pendown()
    t.write("Wrong", font=("Arial",30,"bold italic"),align="center")


t. hideturtle()
turtle.done()