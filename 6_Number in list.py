# coding: utf-8

# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal
# to the proceeding number, the proceeding number should be inserted
# into a sublist.
# Continue adding to the sublist until the proceeding number
# is greater than the first number before the sublist.
# Then add this bigger number to the normal list.

# Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    List = []
    sublist = []

    for x in string:
        num = int(x)
        if len(List) == 0:
            test = num
            List.append(num)
        elif num <= test:
            sublist.append(num)
        elif num > test:
            if len(sublist) > 0:
                List.append(sublist)
            List.append(num)
            test = num
            sublist = []
    if len(sublist) > 0:
        List.append(sublist)
    return List


# testcases
string1 = '543987'
result = [5, [4, 3], 9, [8, 7]]
print repr(string1), numbers_in_lists(string1) == result
string1 = '987654321'
result = [9, [8, 7, 6, 5, 4, 3, 2, 1]]
print repr(string1), numbers_in_lists(string1) == result
string1 = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string1), numbers_in_lists(string1) == result
string1 = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string1), numbers_in_lists(string1) == result
