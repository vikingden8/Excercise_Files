#!/usr/bin/python3


def main():
    x = 43
    print(x, " ", id(x), " ", type(x))
    x = 43.8
    print(x, " ", id(x), " ", type(x))
    x = int(x)
    print(x, " ", id(x), " ", type(x))
    x = 43 / 8
    print(x, " ", id(x), " ", type(x))
    x = 43 // 8
    print(x, " ", id(x), " ", type(x))
    x = round(43 / 8)
    print(x, " ", id(x), " ", type(x))
    x = round(43 / 8, 2)
    print(x, " ", id(x), " ", type(x))

if __name__ == '__main__':
    main()