#!/usr/bin/python3


def main():
    choices = dict(
        one='first',
        two='second',
        three='third',
        four='fourth',
        five='fifth'
    )

    print(choices['two'])
    
    # if we choice one not exist in dictionary, will raise a errr
    # print(choices['seven']
    # but we can use .get(key, default) method
    print(choices.get('seven', 'other'))

if __name__ == '__main__':
    main()