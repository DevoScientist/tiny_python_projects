#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@localhost>
Date   : 2023-07-01
Purpose: Choose the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    # parser.add_argument('-s',
    #                     '--side',
    #                     help='Which side of ship the thing is present',
    #                     metavar='str',
    #                     type=str,
    #                     default='larboard')

    parser.add_argument('-sb',
                        '--starboard',
                        help='present on starboard side',
                        nargs='?',
                        type=bool,
                        const= True,
                        default= False
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    word = args.word
    side = args.starboard
    #T1.......................................................
    # article = ''
    # if word[0].lower() in 'aeiou':
    #     article = 'an'
    # else:
    #     article = 'a'

    #T2.......................................................
    # article = 'a'
    # if word[0].lower() in 'aeiou':
    #     article = 'an'

    #T3.......................................................
    if word[0].islower():
        article = 'an' if word[0] in 'aeiou' else 'a'
    else:
        article = 'An' if word[0].lower() in 'aeiou' else 'A'
    

    # print('Ahoy, Captain, ' + article + ' ' + word + ' off the larboard bow!')

    # print('Ahoy, Captain, {} {} off the larboard bow!'.format(article , word))  # string formatting

    # print(f'Ahoy, Captain, {article} {word} off the {side} bow!')  # string formatting using f-string.
    
    if side:
        print(f'Ahoy, Captain, {article} {word} off the starboard bow!')
    else:
        print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
