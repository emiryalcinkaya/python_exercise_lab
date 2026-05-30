"""
Check whether a number is prime or not.
"""

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime")

else:
    print("Not Prime")