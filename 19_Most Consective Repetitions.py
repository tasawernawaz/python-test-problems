# coding: utf-8


# Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(li):
    if len(li) == 0:
        return
    curr_ele = li[1]
    curr_count = 0
    longest_count = 0
    longest_ele = li[1]
    for x in li:
        if curr_count > longest_count:
            longest_count = curr_count
            longest_ele = curr_ele

        if x == curr_ele:
            curr_count += 1
        else:
            curr_ele = x
            curr_count = 1
    return longest_ele

# For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1, 2, 3, 4, 5])
# 1

print longest_repetition([])
# None
