#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@localhost>
Date   : 2023-07-12
Purpose: Word Count
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Word Count',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        nargs='*',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])
    
    parser.add_argument('-c',
                        '--char',
                        help='For number of characters',
                        metavar='Bool',
                        type= bool,
                        default=False)
    parser.add_argument('-l',
                        '--char',
                        help='For number of characters',
                        metavar='Bool',
                        type= bool,
                        default=False)
    parser.add_argument('-w',
                        '--char',
                        help='For number of characters',
                        metavar='Bool',
                        type= bool,
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    tot_lines, tot_words, tot_bytes = 0, 0, 0
    
    for fh in args.file:

        num_lines = 0
        num_words = 0
        num_bytes = 0

        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        if args.w and args.c:
            
        
            print(f'{num_words:8}{num_bytes:8} {fh.name}')
        elif args.c:
            print(f'{num_bytes:8} {fh.name}')
        elif args.l:
            print(f'{num_lines} {fh.name}')
        elif args.w:
            print(f"{num_words} {fh.name}")
        else:
            print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes

    if len(args.file) > 1:
        print(f'{tot_lines:8}{tot_words:8}{tot_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
