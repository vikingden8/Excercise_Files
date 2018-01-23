#!/usr/bin/python3


def main():
    num = 5
    print(num + 1)
    print(num - 3)
    print(num * 2)
    print(num / 2)
    print(num // 2)
    print(num % 2)
    print(num ** 2)

    num += 2
    print(num)

    num -= 3
    print(num)

    num *= 3
    print(num)

    num //= 2
    print(num)

    num *= 6
    num /= 3
    print(num)


if __name__ == '__main__':
    main()