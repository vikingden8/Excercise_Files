#!/usr/bin/python3


def main():
    # for files
    fh = open("lines.txt")
    for line in fh.readlines():
        print(line, end="")

    # for collections, like list
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    for number in list:
        print(number)

    # for strings
    content = "This is a line of text."
    for char in content:
        print(char, end=" ")
if __name__ == '__main__':
    main()