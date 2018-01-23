#!/usr/bin/python3


def main():
    try:
        for line in readfile('lines.doc'):
            print(line.strip())
    except IOError as e:
        print("There is an exception: {}".format(e.strerror))
    except ValueError as e:
        print('There is an exception:{}'.format(e))


def readfile(filename):
    if filename.endswith(".txt"):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('filename must be end with .txt')

if __name__ == '__main__':
    main()