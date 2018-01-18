#!/usr/bin/python


def main():
    content = "This is a line of text."
    for ch in content:
        print(ch, end="")
    print('')

    # break keywords
    for ch in content:
        if ch == 'o':
            break
        print(ch, end='')
    print('')

    # continue keywords
    for ch in content:
        if ch == 'o':
            continue
        print(ch, end='')
    print('')

    # else keywords
    for ch in content:
        print(ch, end='')
    else:
        print('\nDone.')

    # else keywords for while loops
    i = 0
    while i < len(content):
        print(content[i], end='')
        i += 1
    else:
        print('\nDone.')


if __name__ == '__main__':
    main()