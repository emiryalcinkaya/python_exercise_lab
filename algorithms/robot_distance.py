"""
Calculate the robot's distance from the starting point after movements.
"""

import math

x = 0
y = 0

while True:
    move = input()

    if move == "":
        break

    direction, steps = move.split()
    steps = int(steps)

    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "RIGHT":
        x += steps
    elif direction == "LEFT":
        x -= steps

distance = math.sqrt(x ** 2 + y ** 2)

print(round(distance))