#!/usr/bin/env python3
"""
Author : Kevin Traster <ktraster@freshgrillfoods.com>
Date   : 2021-03-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument(
        "-f",
        "--file",
        help="Input FIle",
        metavar="FILE",
        type=argparse.FileType('rt'),
        default='gashlycrumb.txt',
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sentance={}
    for line in args.file:
        # print(line[0],line,end='')
        sentance[line[0].lower()] = line

    for letter in args.letter:
        if letter.lower() in sentance:
            print (sentance[letter.lower()],end='')
        else:
            print (f'I do not know "{letter}".')
# --------------------------------------------------
if __name__ == '__main__':
    main()
