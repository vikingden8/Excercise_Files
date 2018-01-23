#!/usr/bin/python3


def main():
    # no exceptions
    fh = open('lines.txt')
    for line in fh:
        print(line.strip())

    # with exceptions
    try:
        fh = open('xlines.txt')
        for line in fh:
            print(line.strip())
    except IOError as e:
        print('There is an exception:{}'.format(e.strerror))

if __name__ == '__main__':
    main()