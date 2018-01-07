#!/usr/bin/python3


def main():
    a, b = 0, 1
    if a > b:
        print('a is greater than b')
    elif a < b:
        print('a is less than b')
    else:
        print('a is equal b')
    # conditional expression
    c = 'a is equal or greater than b' if a > b else 'a is less than b '
    print(c)

if __name__ == '__main__':
    main()
