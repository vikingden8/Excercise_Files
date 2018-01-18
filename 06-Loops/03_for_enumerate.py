#!/usr/bin/python3


def main():
    # for files
    fh = open("lines.txt")
    for index, line in enumerate(fh.readlines()):
        print(index, line)

    # for string
    content = "This is a line of text."
    for i, c in enumerate(content):
        print(i, c)

    for i, c in enumerate(content):
        if c == 's':
            print("index {} content is s.".format(i))

if __name__ == '__main__':
    main()