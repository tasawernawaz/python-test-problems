# coding: utf-8

# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB
# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def convert_seconds(number):
    time = ''
    hrs = int(number / 3600)
    mins = int((number - hrs * 3600) / 60)
    secs = int(number - hrs * 3600 - mins * 60)
    time = time + str(secs) + ' hour ' if hrs == 1 else 'hours'
    time = time + str(secs) + ' minute ' if mins == 1 else 'minutes'
    time = time + str(secs) + ' second ' if secs == 1 else 'seconds'

    return time


def download_time(filesize, fileUnit, BandWidth, BandWiddthUnit, ):
    if fileUnit == 'kb':
        filesize *= 2 ** 10
    elif fileUnit == 'kB':
        filesize *= 2 ** 10 * 8
    elif fileUnit == 'Mb':
        filesize *= 2 ** 20
    elif fileUnit == 'MB':
        filesize *= 2 ** 20 * 8
    elif fileUnit == 'Gb':
        filesize *= 2 ** 30
    elif fileUnit == 'GB':
        filesize *= 2 ** 30 * 8
    elif fileUnit == 'Tb':
        filesize *= 2 ** 40
    elif fileUnit == 'TB':
        filesize *= 2 ** 40 * 8

    if BandWiddthUnit == 'kb':
        BandWidth *= 2 ** 10
    elif BandWiddthUnit == 'kB':
        BandWidth *= 2 ** 10 * 8
    elif BandWiddthUnit == 'Mb':
        BandWidth *= 2 ** 20
    elif BandWiddthUnit == 'MB':
        BandWidth *= 2 ** 20 * 8
    elif BandWiddthUnit == 'Gb':
        BandWidth *= 2 ** 30
    elif BandWiddthUnit == 'GB':
        BandWidth *= 2 ** 30 * 8
    elif BandWiddthUnit == 'Tb':
        BandWidth *= 2 ** 40
    elif BandWiddthUnit == 'TB':
        BandWidth *= 2 ** 40 * 8

    return convert_seconds(filesize / BandWidth)


print download_time(1024, 'kB', 1, 'MB')
# >>> 0 hours, 0 minutes, 1 second

print download_time(1024, 'kB', 1, 'Mb')
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13, 'GB', 5.6, 'MB')
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13, 'GB', 5.6, 'Mb')
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10, 'MB', 2, 'kB')
# >>> 1 hour, 25 minutes, 20 seconds  
# 20.0 seconds is also acceptable

print
download_time(10, 'MB', 2, 'kb')
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
