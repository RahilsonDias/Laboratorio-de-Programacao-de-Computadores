import turtle
import random

# Player setups
taro_one = turtle.Turtle()
taro_one.color("green")
taro_one.shape("turtle")
taro_one.penup()
taro_one.goto(-200, 100)

taro_two = taro_one.clone()
taro_two.color("blue")
taro_two.penup()
taro_two.goto(-200, -100)

# Home setups
taro_one.goto(300, 60)
taro_one.pendown()
taro_one.circle(40)
taro_one.penup()
taro_one.goto(-200, 100)

taro_two.goto(300, -140)
taro_two.pendown()
taro_two.circle(40)
taro_two.penup()
taro_two.goto(-200, -100)

# Die
die = [1, 2, 3, 4, 5, 6]

# Game
for i in range(20):

    # Victory conditions
    if taro_one.pos() >= (300, 100):
        print("Player 1 won, congratulations!")
        break

    elif taro_one.pos() >= (300, -100):
        print("Player 2 won, congratulations!")
        break

    # Main game loop
    else:
        taro_one_turn = input("Player 1's turn, press Enter to roll the die!")
        die_result = random.choice(die)
        print(f"You rolled a {die_result}! Move {20 * die_result} steps!")
        taro_one.fd(20*die_result)

        taro_two_turn = input("Player 2's turn, press Enter to roll the die!")
        die_result = random.choice(die)
        print(f"You rolled a {die_result}! Move {20 * die_result} steps!")
        taro_two.fd(20*die_result)

turtle.done()
