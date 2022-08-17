# coding: utf-8

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

import numpy as np


def symmetric(matrix):

    mat = np.array(matrix)
    for i in range(len(matrix)):
        row = list(mat[i])
        col = list(mat[:, i])
        if row == col:
            continue
        else:
            return False

    return True

print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
# >>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]])
# >>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]])
# >>> False

print symmetric([[1, 2],
                 [2, 1]])
# >>> True

print symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]])
# >>> False

print symmetric([[1, 2, 3],
                 [2, 3, 1]])
# >>> False
