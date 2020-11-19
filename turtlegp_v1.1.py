import turtle
import math
import random
import time
import winsound

winsound.PlaySound("opening.wav",winsound.SND_ASYNC)

song = ("1-Tokyo Drift")
song2 = ("2-Buttercup")
song3 = ("3-Self Control")
liste = [song,song2,song3]

muzik = turtle.Screen()
muzik.bgcolor("navy")
muzik.title("Hangi müzikle oynamak istersin?")
secim = muzik.numinput("Şarkılar;",liste)

if secim == 1:
    winsound.PlaySound("song.wav",winsound.SND_ASYNC)
if secim == 2:
    winsound.PlaySound("song2.wav",winsound.SND_ASYNC)
elif secim == 3:
    winsound.PlaySound("song3.wav",winsound.SND_ASYNC)

#ekran olusturma ve ayarlari
arkaplan = turtle.Screen()
arkaplan.bgcolor("grey")
arkaplan.title("Welcome to Turtle Grand Prix")

rule = turtle.Turtle()
rule.hideturtle()
rule.penup()
rule.setposition(0,360)
rule.color("white")
rule.write("You must pass the green control point last for the current time value.")

rule2 = turtle.Turtle()
rule2.hideturtle()
rule2.penup()
rule2.setposition(0,375)
rule2.color("white")
rule2.write("There are 12 control points to passing.")

rule3 = turtle.Turtle()
rule3.hideturtle()
rule3.penup()
rule3.setposition(-300,360)
rule3.color("white")
rule3.write("Created by Batuhan OĞLAKÇIOĞLU - Have Fun ! ")

#turtle olusturma ve ayarlari
oyuncu = turtle.Turtle()
oyuncu.color("white")
oyuncu.shape("turtle")
oyuncu.speed(0.5)
oyuncu.penup()
scoreoyuncu1 = 0

#border olusturma
mypen = turtle.Turtle()
mypen.color("yellow")
mypen.penup()
mypen.setposition(-350,-350)
mypen.pendown()
mypen.pensize(4)
for side in range (4):
    mypen.forward(700)
    mypen.left(90)
mypen.hideturtle()

#degiskenler
speed1 = 2.5

#fonksiyonlar
def turnleft():
    oyuncu.left(30)
def turnright():
    oyuncu.right(30)

#klavye tanimlamalari
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")

#goals
a1 = turtle.Turtle()
a1.turtlesize(1)
a1.color("royal blue")
a1.shape("classic")
a1.penup()
a1.speed(0)
a1.setposition(random.randint(-345,345),random.randint(-345,345))

a2 = turtle.Turtle()
a2.turtlesize(1)
a2.color("purple")
a2.shape("classic")
a2.penup()
a2.speed(0)
a2.setposition(random.randint(-345,345),random.randint(-345,345))

a3 = turtle.Turtle()
a3.turtlesize(1)
a3.color("lightblue")
a3.shape("classic")
a3.penup()
a3.speed(0)
a3.setposition(random.randint(-345,345),random.randint(-345,345))

a4 = turtle.Turtle()
a4.turtlesize(1)
a4.color("gold")
a4.shape("classic")
a4.penup()
a4.speed(0)
a4.setposition(random.randint(-345,345),random.randint(-345,345))

a5 = turtle.Turtle()
a5.turtlesize(1)
a5.color("skyblue")
a5.shape("classic")
a5.penup()
a5.speed(0)
a5.setposition(random.randint(-345,345),random.randint(-345,345))

a6 = turtle.Turtle()
a6.turtlesize(1)
a6.color("maroon")
a6.shape("classic")
a6.penup()
a6.speed(0)
a6.setposition(random.randint(-345,345),random.randint(-345,345))

a7 = turtle.Turtle()
a7.turtlesize(1)
a7.color("orange")
a7.shape("classic")
a7.penup()
a7.speed(0)
a7.setposition(random.randint(-345,345),random.randint(-345,345))

a8 = turtle.Turtle()
a8.turtlesize(1)
a8.color("navy")
a8.shape("classic")
a8.penup()
a8.speed(0)
a8.setposition(random.randint(-345,345),random.randint(-345,345))

a9 = turtle.Turtle()
a9.turtlesize(1)
a9.color("magenta")
a9.shape("classic")
a9.penup()
a9.speed(0)
a9.setposition(random.randint(-345,345),random.randint(-345,345))

a10 = turtle.Turtle()
a10.turtlesize(1)
a10.color("lime")
a10.shape("classic")
a10.penup()
a10.speed(0)
a10.setposition(random.randint(-345,345),random.randint(-345,345))

a11 = turtle.Turtle()
a11.turtlesize(1)
a11.color("pink")
a11.shape("classic")
a11.penup()
a11.speed(0)
a11.setposition(random.randint(-345,345),random.randint(-345,345))

a12=turtle.Turtle()
a12.turtlesize(1)
a12.color("dark turquoise")
a12.shape("classic")
a12.penup()
a12.speed(0)
a12.setposition(random.randint(-345,345),random.randint(-345,345))

#5 red lights to start

r1 = turtle.Turtle()
r1.penup()
r1.shape("circle")
r1.turtlesize(3)
r1.color("red")
r1.speed(0)
r1.setposition(-200,0)

time.sleep(1)

r2 = turtle.Turtle()
r2.penup()
r2.shape("circle")
r2.turtlesize(3)
r2.color("red")
r2.speed(0)
r2.setposition(-100,0)

time.sleep(1)

r3 = turtle.Turtle()
r3.penup()
r3.shape("circle")
r3.turtlesize(3)
r3.color("red")
r3.speed(0)
r3.setposition(0,0)

time.sleep(1)

r4 = turtle.Turtle()
r4.penup()
r4.shape("circle")
r4.turtlesize(3)
r4.color("red")
r4.speed(0)
r4.setposition(100,0)

time.sleep(1)

r5 = turtle.Turtle()
r5.penup()
r5.shape("circle")
r5.turtlesize(3)
r5.color("red")
r5.speed(0)
r5.setposition(200,0)

time.sleep(1)

r1.hideturtle()
r2.hideturtle()
r3.hideturtle()
r4.hideturtle()
r5.hideturtle()

#sayac
starttime = time.time()


#loop

while True:
    oyuncu.forward(speed1)
    """oyuncu2.forward(0)"""
    
    if oyuncu.xcor() > 345 or oyuncu.xcor() < -345:
        oyuncu.right(180)
    if oyuncu.ycor() > 345 or oyuncu.ycor() < -345:
        oyuncu.right(180)
        
    #carpisma
    d1 = math.sqrt(math.pow(oyuncu.xcor()-a1.xcor(),2) + math.pow(oyuncu.ycor()-a1.ycor(),2))
    if d1 < 10:
        a1.hideturtle()
        scoreoyuncu1 = scoreoyuncu1 + 1
        
    d2 = math.sqrt(math.pow(oyuncu.xcor()-a2.xcor(),2) + math.pow(oyuncu.ycor()-a2.ycor(),2))
    if d2 < 10:
        a2.hideturtle()
        scoreoyuncu1 +=1
        
    d3 = math.sqrt(math.pow(oyuncu.xcor()-a3.xcor(),2) + math.pow(oyuncu.ycor()-a3.ycor(),2))
    if d3 < 10:
        a3.hideturtle()
        scoreoyuncu1 +=1
        
    d4 = math.sqrt(math.pow(oyuncu.xcor()-a4.xcor(),2) + math.pow(oyuncu.ycor()-a4.ycor(),2))
    if d4 < 10:
        a4.hideturtle()
        scoreoyuncu1 +=1
        
    d5 = math.sqrt(math.pow(oyuncu.xcor()-a5.xcor(),2) + math.pow(oyuncu.ycor()-a5.ycor(),2))
    if d5 < 10:
        a5.hideturtle()
        scoreoyuncu1 +=1
        
    d6 = math.sqrt(math.pow(oyuncu.xcor()-a6.xcor(),2) + math.pow(oyuncu.ycor()-a6.ycor(),2))
    if d6 < 10:
        a6.hideturtle()
        scoreoyuncu1 +=1
        
    d7 = math.sqrt(math.pow(oyuncu.xcor()-a7.xcor(),2) + math.pow(oyuncu.ycor()-a7.ycor(),2))
    if d7 < 10:
        a7.hideturtle()
        scoreoyuncu1 +=1
        
    d8 = math.sqrt(math.pow(oyuncu.xcor()-a8.xcor(),2) + math.pow(oyuncu.ycor()-a8.ycor(),2))
    if d8 < 10:
        a8.hideturtle()
        scoreoyuncu1 +=1
        
    d9 = math.sqrt(math.pow(oyuncu.xcor()-a9.xcor(),2) + math.pow(oyuncu.ycor()-a9.ycor(),2))
    if d9 < 10:
        a9.hideturtle()
        scoreoyuncu1 +=1
        
    d11 = math.sqrt(math.pow(oyuncu.xcor()-a11.xcor(),2) + math.pow(oyuncu.ycor()-a11.ycor(),2))
    if d11 < 10:
        a11.hideturtle()
        scoreoyuncu1 +=1
        
    d12 = math.sqrt(math.pow(oyuncu.xcor()-a12.xcor(),2) + math.pow(oyuncu.ycor()-a12.ycor(),2))
    if d12 < 10:
        a12.hideturtle()
        scoreoyuncu1 +=1    
        
    d10 = math.sqrt(math.pow(oyuncu.xcor()-a10.xcor(),2) + math.pow(oyuncu.ycor()-a10.ycor(),2))
    
    if d10 < 10 and scoreoyuncu1 > 80:
        a10.hideturtle()
        endtime = time.time()
        duration = int(endtime - starttime)
        print("--------------------------")
        print("You finished Turtle GP in ",end="")
        print(duration,end="")
        print(" seconds")
        exit()
               
oyuncu.mainloop()

delay = raw_input("Lütfen bir tuşa basiniz.")    