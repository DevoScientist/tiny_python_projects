#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@localhost>
Date   : 2023-07-05
Purpose: Jump The 5 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump The 5 ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    jumper = {
        '1' : '9',
        '2' : '8',
        '3' : '7',
        '4' : '6',
        '5' : '0',
        '6' : '4',
        '7' : '3',
        '8' : '2',
        '9' : '1',
        '0' : '5'
    }

    # list = []
    # for char in text:
    #     # if char in jumper.keys():
    #     #     print(jumper.get(char), end='')
    #     # else:
    #     #     print(char, end='')

    #     # print(jumper.get(char, char), end = '')

    #     list.append(jumper.get(char, char))
    # print(''.join(list))
    # print()

    # print(''.join([jumper.get(char, char) for char in text]))
    print(text.translate(str.maketrans(jumper)))
# --------------------------------------------------
if __name__ == '__main__':
    main()
