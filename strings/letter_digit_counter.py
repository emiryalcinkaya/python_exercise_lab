"""
Count letters and digits in a sentence.
"""

text = input("Enter a sentence: ")

counts = {
    "LETTERS": 0,
    "DIGITS": 0
}

for character in text:
    if character.isalpha():
        counts["LETTERS"] += 1
    elif character.isdigit():
        counts["DIGITS"] += 1

print("Letters: ", counts["LETTERS"])
print("Digits: ", counts["DIGITS"])