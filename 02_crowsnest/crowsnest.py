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
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    if word[0].islower():
        article = 'an' if word[0].lower() in 'aeiou' else 'a'
    else:
        article = 'An' if word[0].lower() in 'aeiou' else 'A'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
