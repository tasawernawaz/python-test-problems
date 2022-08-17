# coding: utf-8

# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(number):
    time = ''
    hrs = int(number / 3600)
    mins = int((number - hrs * 3600) / 60)
    secs = int(number - hrs * 3600 - mins * 60)
    if hrs == 1:
        time = time + str(hrs) + ' hour '
    else:
        time = time + str(hrs) + ' hours '
    if mins == 1:
        time = time + str(mins) + ' minute '
    else:
        time = time + str(mins) + ' minutes '
    if secs == 1:
        time = time + str(secs) + ' second '
    else:
        time = time + str(secs) + ' seconds '
    return time

print convert_seconds(3661)
# >>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
# >>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
# >>> 2 hours, 1 minute, 1.7 seconds
