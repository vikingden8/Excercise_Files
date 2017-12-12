#!/usr/bin/python3

try:
    f = open('xlines.txt')
    for line in f.readlines():
        print(line, end='')
except IOError as e:
    print('Some bad thing happened: ({})'.format(e))

print('Do after badness.')