#!/usr/bin/python3

f = open("lines.txt")

for line in f.readlines():
    print(line, end="")
