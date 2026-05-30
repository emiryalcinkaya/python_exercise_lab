"""
Find binary numbers that are divisible by 5.
"""

binary_numbers = input().split(",")

result = []

for binary_number in binary_numbers:
    decimal_number = int(binary_number, 2)

    if decimal_number % 5 == 0:
        result.append(binary_number)

print(",".join(result))