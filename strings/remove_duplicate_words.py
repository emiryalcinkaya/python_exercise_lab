"""
Remove duplicate words from a sentence and sort them alphabetically.
"""

sentence = input("Enter your sentences: ")

words = sentence.split()

unique_words = sorted(set(words))

print(" ".join(unique_words))