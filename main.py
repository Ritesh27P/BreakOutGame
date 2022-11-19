import turtle
from blocks import Block

screen = turtle.Screen()
screen.bgcolor('black')
screen.screensize(600, 600)

wt = turtle.Turtle()

score = 0

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

def move_right():
    player.fd(5)

def move_left():
    player.backward(5)

screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.listen()

position = [(-300, 300), (-270, 300), (-240, 300), (-210, 300), (-180, 300), (-150, 300), (-120, 300), (-90, 300), (-60, 300), (-30, 300), 
            (0, 300), (30, 300), (60, 300), (90, 300),  (120, 300), (150, 300), (180, 300), (210, 300), (240, 300), (270, 300), (300, 300),
            (-300, 275), (-270, 275), (-240, 275), (-210, 275), (-180, 275), (-150, 275), (-120, 275), (-90, 275), (-60, 275), (-30, 275), (0, 275),
            (30, 275), (60, 275), (90, 275),  (120, 275), (150, 275), (180, 275), (210, 275), (240, 275), (270, 275), (300, 275),
            (-300, 250), (-270, 250), (-240, 250), (-210, 250), (-180, 250), (-150, 250), (-120, 250), (-90, 250), (-60, 250), (-30, 250), 
            (0, 250), (30, 250), (60, 250), (90, 250),  (120, 250), (150, 250), (180, 250), (210, 250), (240, 250), (270, 250), (300, 250)]

blocks = []
# position = [(0,0)]

turtle.tracer(False)
for i in position:
    tt = Block(i)
    blocks.append(tt)
turtle.tracer(True)

ball = turtle.Turtle('circle')
ball.speed(1.5)
ball.penup()
ball.goto(0, -300)
ball.setheading(145)
ball.color('white')

player = turtle.Turtle('square')
player.goto(0, -300)
player.penup()
player.color('white')
player.resizemode('user')
player.shapesize(2, 8, 2)

game_on = True
while game_on:
    ball.fd(10)
    x, y = ball.pos()
    for i in blocks:
        if is_collided_with(ball, i):
            score += 1
            if ball.heading() > 0 and ball.heading() < 90:
                i.hideturtle()
                i.goto(-500, 300)
                ball.seth(315)
            else:
                i.hideturtle()
                ball.seth(225)
    print(player.pos())
    if abs(ball.xcor() - player.xcor()) < 70 and abs(ball.ycor() - player.ycor()) < 16:
        if ball.heading() > 90 and ball.heading() < 270:
            ball.setheading(135)
        else:
            ball.setheading(45)

    if x > 320.0:
        print(ball.heading())
        if ball.heading() > 0.0 and ball.heading() <180.0:
            ball.setheading(135)
        else:
            ball.setheading(225)
    if y > 320.0:
        break
    if x < -320.0:
        if ball.heading() > 0.0 and ball.heading() <180.0:
            ball.seth(45)
        else:
            ball.seth(315)
    if y < -340.0:
        
        wt.goto(-25,0)
        wt.pencolor('green')
        wt.hideturtle()
        wt.write(f'GAME Over\nScore : {score}', font=['Times', 30])
        
        break

screen.mainloop()
