#!/usr/bin/python3


def main():
    # define a tuple
    tuple = (1, 2, 3)
    print(type(tuple), tuple)

    # define a list
    list = [5, 6, 7]
    print(type(list), list)

    text = "wonderful"
    print(type(text), text[2:4])

    for ch in text:
        print(ch, end=' ')


if __name__ == '__main__':
    main()