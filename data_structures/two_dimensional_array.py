"""
Generate a two-dimensional array where each element
is the product of its row and column indexes.
"""

values = input().split(",")

rows = int(values[0])
columns = int(values[1])

matrix = [[0 for column in range(columns)] for row in range(rows)]

for row in range(rows):
    for column in range(columns):
        matrix[row][column] = row * column

print(matrix)