import turtle
import math


def draw_fibonacci(n):
    a = 0
    b = 1

    # Turtle setup
    taro.shape("turtle")
    taro.pencolor("red")

    # Draw first square
    taro.forward(b)
    taro.left(90)
    taro.forward(b)
    taro.left(90)
    taro.forward(b)
    taro.left(90)
    taro.forward(b)

    # Progress Fibonacci
    fibo = a + b
    a = b
    b = fibo

    # Draw remaining squares
    for i in range(1, n):
        taro.backward(a * upscale)
        taro.right(90)
        taro.forward(fibo * upscale)
        taro.left(90)
        taro.forward(fibo * upscale)
        taro.left(90)
        taro.forward(fibo * upscale)

        # Progress Fibonacci
        fibo = a + b
        a = b
        b = fibo

    # Move pen to start position
    taro.penup()
    taro.setposition(upscale, 0)
    taro.seth(90)
    taro.pendown()

    # Turtle setup
    taro.pencolor("blue")

    # Parameter setup
    a = 0
    b = 1
    fibo = b

    # Draw Fibonacci spiral
    for i in range(n):
        print(fibo)
        arcsize = math.pi * fibo * upscale / 2
        stepsize = arcsize/90

        for j in range(90):
            taro.forward(stepsize)
            taro.left(1)
        fibo = a + b
        a = b
        b = fibo


n = int(input("Enter the number of iterations: "))
upscale = 2

if n > 0:
    print(f"Fibonacci series for {n} elements: ")
    taro = turtle.Turtle()
    taro.speed(100)
    draw_fibonacci(n)
    turtle.done()

else:
    print("Invalid entry")
