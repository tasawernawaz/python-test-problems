# coding: utf-8

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n,
# and returns the string constructed
# by shifting each of the letters n steps, and
# leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an
# additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    return chr(ord('a') + (ord(letter) - ord('a') + n) % 26)


def rotate(string, number):
    rotatedstring = ''
    for i in string:
        if i != ' ':
            rotatedstring += shift_n_letters(i, number)
        else:
            rotatedstring += ' '
    return rotatedstring


print(rotate('sarah', 13))
# >>> 'fnenu'
print(rotate('fnenu', 13))
# >>> 'sarah'
print(rotate('dave', 5))
# >>>'ifaj'
print(rotate('ifaj', -5))
# >>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
# >>> if your code works correctly you should be able to read this
