#!/usr/bin/env python3
"""
Author : Kevin Traster <ktraster@freshgrillfoods.com>
Date   : 2021-03-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str", metavar="str", help="Input Text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    pos_arg = args.str

    # print(f"{pos_arg}")
    jumper = dict()
    jumper["1"] = "9"
    jumper["2"] = "8"
    jumper["3"] = "7"
    jumper["4"] = "6"
    jumper["5"] = "0"
    jumper["6"] = "4"
    jumper["7"] = "3"
    jumper["8"] = "2"
    jumper["9"] = "1"
    jumper["0"] = "5"

    for char in pos_arg:
        print(jumper.get(char, f"{char}"), end="")
    # print()


# --------------------------------------------------
if __name__ == "__main__":
    main()
