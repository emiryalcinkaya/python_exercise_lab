"""
Generate all permutations of a list.
"""

import itertools

numbers = [1, 2, 3]

permutations = list(itertools.permutations(numbers))

print(permutations)