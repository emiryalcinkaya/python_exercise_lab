"""
Create a Rectangle class and calculate its area.
"""

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(5, 10)

print(rectangle.area())