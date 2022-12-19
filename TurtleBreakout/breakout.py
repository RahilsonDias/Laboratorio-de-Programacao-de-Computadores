import turtle
import winsound


x_list = [-320, -271, -222, -173, -124, -75, -26, 23, 72, 121, 170, 219, 267, 314]
y_list = [250, 235, 220, 205, 190, 175, 160, 145]
colors = ['yellow', 'green', 'orange', 'red']
brick_list = []


def draw_bricks():
    for j in y_list:
        for k in x_list:
            brick = turtle.Turtle()
            brick.shape('square')
            brick.shapesize(stretch_wid=0.5, stretch_len=2)
            if j <= 160:
                brick.c = colors[0]
            elif j <= 190:
                brick.c = colors[1]
            elif j <= 220:
                brick.c = colors[2]
            else:
                brick.c = colors[3]
            brick.color(brick.c)
            brick.up()
            brick.goto(k, j)
            brick.state = 'ready'
            brick_list.append(brick)


# left movement
def paddle_left():
    x = paddle.xcor()
    new_x = x - 30
    if new_x > -285:
        x += -30
    else:
        x += -abs(x + 290)
    paddle.setx(x)


# right movement
def paddle_right():
    x = paddle.xcor()
    new_x = x + 30
    if new_x < 284:
        x += 30
    else:
        x += abs(x - 284)
    paddle.setx(x)


# draw screen
screen = turtle.Screen()
screen.title("TurtleBreakout")
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.tracer(0)


# draw border
border = turtle.Turtle()
border.color("white")
border.penup()
border.setposition(-345, -340)
border.pendown()
border.speed(100)
border.left(90)
border.pensize(10)
border.forward(685)
border.right(90)
border.pensize(25)
border.forward(685)
border.right(90)
border.pensize(10)
border.forward(685)
border.right(90)
border.pensize(25)
border.forward(685)
border.hideturtle()

# draw paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=0.5, stretch_len=5)
paddle.penup()
paddle.goto(0, -310)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0, 50)
ball.dx = 1
ball.dy = -1

# score
score = 0
balls_left = 3

# hud
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 280)
hud.write("Balls left: 3   Score: 0", align="center", font=("Press Start 2P", 15, "normal"))

# bricks
draw_bricks()

# keyboard
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

while balls_left > 0:
    if len(brick_list) > 0:
        screen.update()

        # ball movement
        ball.setx(ball.xcor() + 3 * ball.dx)
        ball.sety(ball.ycor() + 3 * ball.dy)

        # collision with the upper wall
        if ball.ycor() > 325:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.sety(325)
            ball.dy *= -1

        # collision with lower wall
        if ball.ycor() <= -340:
            balls_left -= 1
            hud.clear()
            hud.write("Balls left: {}   Score: {}".format(balls_left, score), align="center",
                      font=("Press Start 2P", 15, "normal"))
            winsound.PlaySound("bleep.wav", winsound.SND_ASYNC)
            ball.goto(0, 50)
            ball.dx = 1
            ball.dy = -1

        # collision with left wall
        if ball.xcor() < -340:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.setx(-335)
            ball.dx *= -1

        # collision with right wall
        if ball.xcor() > 335:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.setx(330)
            ball.dx *= -1

        # collision with the paddle
        if ball.ycor() < -300 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.dy = abs(ball.dy)

        # collision with the blocks
        for brick_i in brick_list:
            if ball.distance(brick_i) < 26:
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
                brick_i.hideturtle()
                brick_list.remove(brick_i)

                # detect collision from left
                if ball.xcor() < brick_i.xcor() - 20:
                    ball.dx = -1 * abs(ball.dx)

                # detect collision from right
                elif ball.xcor() > brick_i.xcor() + 20:
                    ball.dx = abs(ball.dx)

                # detect collision from bottom
                elif ball.ycor() < brick_i.ycor() - 5:
                    ball.dy = -1 * abs(ball.dy)

                # detect collision from top
                elif ball.ycor() > brick_i.ycor() + 5:
                    ball.dy = abs(ball.dy)

                if brick_i.color()[0] == "yellow":
                    score += 1
                elif brick_i.color()[0] == "green":
                    score += 3
                elif brick_i.color()[0] == "orange":
                    score += 5
                elif brick_i.color()[0] == "red":
                    score += 7

                hud.clear()
                hud.write("Balls left: {}   Score: {}".format(balls_left, score), align="center",
                          font=("Press Start 2P", 15, "normal"))
    else:
        ball.goto(0, 50)
        ball.dx = 1
        ball.dy = -1
        draw_bricks()

hud.clear()
hud.write("Game Over    Final Score: {}".format(score), align="center",
          font=("Press Start 2P", 15, "normal"))
screen.exitonclick()
