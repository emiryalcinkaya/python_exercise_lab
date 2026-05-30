"""
Count the frequency of each word in a sentence.
"""

text = input("Enter a sentence: ")

word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

for word in sorted(word_count):
    print(f"{word}: {word_count[word]}")