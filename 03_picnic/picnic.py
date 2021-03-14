#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2021-03-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic Game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("str", metavar="str", nargs="+", help="Items(s) to bring")

    parser.add_argument(
        "-s",
        "--sorted",
        dest="sort",
        default="False",
        const="true",
        help="Sort the items",
        action="store_const",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.str
    sort_arg = args.sort
    item_length = len(str_arg)

    if sort_arg == "true":
        str_arg.sort()
    if item_length == 1:
        print(f"You are bringing {str_arg[0]}.")
    elif item_length == 2:
        print(f"You are bringing {str_arg[0]} and {str_arg[1]}.")
    else:
        allitems = ", ".join(str_arg[:-1])
        print(f"You are bringing {allitems} and {str_arg[-1]}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
