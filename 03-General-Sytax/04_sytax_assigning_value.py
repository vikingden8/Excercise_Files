#!/usr/bin/python

def main():
    a, b = 0, 1
    print(a, b)
    a, b = b, a
    print(a, b)
    a = (1, 2, 3, 4, 5)
    print(type(b))
    print(type(a), a)
    b = [1, 2, '34', 'text']
    print(type(b), b)

if __name__ == '__main__': main()
