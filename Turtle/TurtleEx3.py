import turtle

taro = turtle.Turtle()

# Turtle setup
taro.shape("turtle")
taro.pencolor("red")


def draw_triangle(x, y):
    # Position the turtle at mouse position
    taro.penup()
    taro.goto(x, y)
    taro.pendown()

    # Draw three small triangles that join to make a big one
    for i in range(3):
        taro.forward(100)
        taro.left(120)
        taro.forward(100)


turtle.onscreenclick(draw_triangle, 1)

turtle.listen()

turtle.done()
