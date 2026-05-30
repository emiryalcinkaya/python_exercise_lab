"""
Sort comma-separated words in alphabetical order.
"""

words = input("Enter words: ").split(",")

words.sort()

print(",".join(words))