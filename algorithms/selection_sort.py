"""
Sort a list using the selection sort algorithm.
"""

def selection_sort(numbers):

    n = len(numbers)

    for i in range(n):

        smallest_index = i

        for j in range(i + 1, n):

            if numbers[j] < numbers[smallest_index]:
                smallest_index = j

        numbers[i], numbers[smallest_index] = (
            numbers[smallest_index],
            numbers[i]
        )

    return numbers


numbers = [64, 25, 12, 22, 11]

print(selection_sort(numbers))