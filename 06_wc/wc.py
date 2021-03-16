#!/usr/bin/env python3
"""
Author : Kevin Traster <ktraster@freshgrillfoods.com>
Date   : 2021-03-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('FILE',
                        help='Input file(s)',
                        nargs="*",
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_words = int(0)
    total_lines =int(0)
    total_bytes =int(0)
    total_files = int(0)
    for fh in args.FILE:
        words = 0.0
        lines =0.0
        bytes =0.0
        for line in fh:
            lines += 1

            words += len(line.split())
            bytes += len(line)


        print (f"{lines:8.0f}{words:8.0f}{bytes:8.0f} {fh.name}")
        total_files +=1
        total_lines += lines
        total_words += words
        total_bytes += bytes
    if total_files > 1:
        print (f"{total_lines:8.0f}{total_words:8.0f}{total_bytes:8.0f} total")


# --------------------------------------------------
if __name__ == '__main__':
    main()
