#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@localhost>
Date   : 2023-07-01
Purpose: going to picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='going to picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to be taken')



    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the item',
                        action='store_true')
    
    parser.add_argument('-no',
                        '--no_oxford',
                        action='store_true',
                        help='print without oxford comma')
    
    parser.add_argument('-c',
                        '--character',
                        metavar='character',
                        type = str,
                        default=',',
                        help='add a character in place of comma comma')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()
    items = args.item
    sorted = args.sorted
    character = args.character + ' '
    if sorted:
        items.sort()

    if len(items) == 1:
        print(f'You are bringing {"".join(items)}.')
    elif len(items) == 2:
        print(f'You are bringing {" and ".join(items)}.')
    else:
        if args.no_oxford:
            print(f'You are bringing {character.join(items[:-2])}{character}{" and ".join(items[-2:])}.') 
        else:
            #print(f'You are bringing {", ".join(items[:len(items)-2])}, {", and ".join(items[len(items)-2:])}.') #__My Style 😁👍__
            # print(f'You are bringing {", ".join(items[:-2])}, {",and ".join(items[-2:])}.')
            print(f'You are bringing {character.join(items[:-1])}{character}and {items[-1]}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
