"""
Generate a dictionary where each key is a number
and each value is the square of that number.
"""

number = int(input())
squares = {}

for value in range(1, number + 1):
    squares[value] = value ** 2

print(squares)