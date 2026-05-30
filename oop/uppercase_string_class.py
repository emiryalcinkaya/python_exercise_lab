"""
Create a class that stores a string and prints it in uppercase.
"""

class InputOutputString:
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Enter text: ")

    def print_uppercase(self):
        print(self.text.upper())


string_object = InputOutputString()
string_object.get_string()
string_object.print_uppercase()