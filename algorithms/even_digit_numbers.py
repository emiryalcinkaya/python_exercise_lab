"""
Find all numbers whose digits are all even.
"""

even_numbers = []

for number in range(1000, 3001):
    digits = str(number)

    if (
        int(digits[0]) % 2 == 0
        and int(digits[1]) % 2 == 0
        and int(digits[2]) % 2 == 0
        and int(digits[3]) % 2 == 0
    ):
        even_numbers.append(digits)

print(",".join(even_numbers))
