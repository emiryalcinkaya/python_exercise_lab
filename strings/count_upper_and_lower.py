"""
Count uppercase and lowercase letters.
"""

text = input("Enter a sentence: ")

counts = {
    "UPPER CASE": 0,
    "LOWER CASE": 0
}

for character in text:
    if character.isupper():
        counts["UPPER CASE"] += 1
    elif character.islower():
        counts["LOWER CASE"] += 1

print("Upper Case: ", counts["UPPER CASE"])
print("Lower Case: ", counts["LOWER CASE"])