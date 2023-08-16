#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@localhost>
Date   : 2023-07-08
Purpose: Howler Exercise...
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases inputs)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    if outfile == '':
        if os.path.isfile(text):
            fh = open(text)
            print(fh.read().upper())
            fh.close()
        else:
            print(text.upper())
    else:
        if os.path.isfile(text):
            fh = open(text)
            out_fh = open(outfile , 'wt')
            out_fh.write(fh.read().upper() + '\n')
            fh.close()
            out_fh.close()
            # print(open(outfile).read())
        else:
            out_fh = open(outfile , 'wt')
            out_fh.write(text.upper() + '\n')
            out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()
