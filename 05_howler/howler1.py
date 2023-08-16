#!/usr/bin/env python3
"""
Author : devoscientist <devoscientist@localhost>
Date   : 2023-07-08
Purpose: My 2nd sol.howler
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My 2nd sol.howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input file or text')

    parser.add_argument('-o',
                        '--outfile',
                        help='output file',
                        metavar='str',
                        type=str,
                        default='')

    

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    
    # print(args.text.upper() , file = out_fh)
    
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
