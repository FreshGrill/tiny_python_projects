#!/usr/bin/env python3
"""
Author : Kevin Traster <ktraster@freshgrillfoods.com>
Date   : 2021-03-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input string of file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="str",
        type=str,
        default="",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    if os.path.isfile(text):
        ftext = open(text).read().strip()
    else:
        ftext = text

    if outfile != "":
        out_fh = open(outfile, "wt")
        out_fh.write(ftext.upper() + "\n")
        out_fh.close()
    else:
        print(ftext.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
