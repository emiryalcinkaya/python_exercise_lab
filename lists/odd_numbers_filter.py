"""
Print only odd numbers from a comma-separated list.
"""

numbers = input("Enter numbers separated by commas: ")

odd_numbers = []

for number in numbers.split(","):
    if int(number) % 2 != 0:
        odd_numbers.append(number)

print(",".join(odd_numbers))