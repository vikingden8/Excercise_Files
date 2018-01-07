#!/usr/bin/python3


def main():
    content = "this is a text"
    print(content)

    x = 45
    content = "this is a format text with number :{}"
    print(content.format(x))

    content = '''\
This is a text
Line after line
more text
'''
    print(content)

if __name__ == '__main__':
    main()