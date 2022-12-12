import turtle

# Turtle setup
turtle.shape("turtle")
turtle.speed(1000)
turtle.right(-90)

angle = 30


def draw_tree(size, level):

    if level > 0:
        # Color gradient setup
        turtle.colormode(255)
        turtle.pencolor(240//level, 115//level, 210//level)

        # Base
        turtle.forward(size)
        turtle.right(angle)

        # Left branch
        draw_tree(0.8 * size, level - 1)
        turtle.pencolor(240//level, 115//level, 210//level)
        turtle.left(2 * angle)

        # Right branch
        draw_tree(0.8 * size, level - 1)
        turtle.pencolor(240//level, 115//level, 210//level)
        turtle.right(angle)
        turtle.forward(-size)


draw_tree(80, 9)
turtle.done()
