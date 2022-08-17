# coding: utf-8

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
# negative or zero.

def shift_n_letters(letter, n):
    asci = ord(letter) + n  # 97-122
    if asci > 122:
        dif = asci - 122
        return chr(dif + 96)
    if asci < 97:
        dif = 97 - asci
        return chr(123 - dif)
    else:
        return chr(asci)


print shift_n_letters('s', 1)
# >>> t
print shift_n_letters('s', 2)
# >>> u
print shift_n_letters('s', 10)
# >>> c
print shift_n_letters('s', -10)
# >>> i
