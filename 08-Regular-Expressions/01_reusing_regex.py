#!/usr/bin/python3
import re


def main():
    fh = open("simple.txt")
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')


if __name__ == '__main__':
    main()