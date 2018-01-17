#!/usr/bin/python3


def main():
    d = {'one': 1, 'two': 2, 'three': 3}
    print(type(d), id(d), d)
    for k in d:
        print(d[k])

    # with sorted keys print
    for k in sorted(d.keys()):
        print(d[k])

    # another way to init dictionary
    d1 = dict(
        one=1,
        two=2,
        three=3
    )
    print(type(d1), id(d1), d1)
    for k in d1:
        print(d1[k])


if __name__ == '__main__':
    main()