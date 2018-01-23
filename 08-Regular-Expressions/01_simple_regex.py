#!/usr/bin/python3
import re


def main():
    fh = open("simple.txt")
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')

    fh = open("simple.txt")
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())


if __name__ == '__main__':
    main()