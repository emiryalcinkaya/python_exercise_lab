"""
Create and use a custom exception class.
"""

class MyError(Exception):

    def __init__(self, message):
        self.message = message


try:
    raise MyError("Something went wrong")

except MyError as error:
    print(error.message)