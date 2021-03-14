#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
import sys
from subprocess import getstatusoutput, getoutput, check_output
import subprocess

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
mixed_words = ['aviso', 'Eel', 'clipper', 'Frigate', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        # rv, out = getstatusoutput(f'{prg} {flag}')
        # assert rv == 0
        # assert out.lower().startswith('usage')
        try:
            output = subprocess.check_output(['python3', prg, flag])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        assert output.decode('utf-8').lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        #   out = getoutput(f'{prg} {word}')
        #  assert out.strip() == template.format('a', word)
        try:
            output = subprocess.check_output(['python3', prg, word])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        assert output.decode('utf-8').strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        # out = getoutput(f'{prg} {word.title()}')
        # assert out.strip() == template.format('a', word.title())
        try:
            output = subprocess.check_output(['python3', prg, word.title()])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        assert output.decode('utf-8').strip() == template.format('A',
                                                                 word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        # out = getoutput(f'{prg} {word}')
        # assert out.strip() == template.format('an', word)
        try:
            output = subprocess.check_output(['python3', prg, word])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        assert output.decode('utf-8').strip() == template.format('an',
                                                                 word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        # out = getoutput(f'{prg} {word.upper()}')
        # assert out.strip() == template.format('an', word.upper())
        try:
            output = subprocess.check_output(['python3', prg, word.upper()])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        assert output.decode('utf-8').strip() == template.format('An',
                                                                 word.upper())
def test_mixed_words():
    """Octopus -> An Octopus"""

    for word in mixed_words:
        # out = getoutput(f'{prg} {word.upper()}')
        # assert out.strip() == template.format('an', word.upper())
        try:
            output = subprocess.check_output(['python3', prg, word])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)


        if word[0].islower():
            prep = 'an' if word[0].lower() in 'aeiou' else 'a'
            assert output.decode('utf-8').strip() == template.format(prep,
                                                                     word)
        else:
            prep = 'An' if word[0].lower() in 'aeiou' else 'A'
            assert output.decode('utf-8').strip() == template.format(prep,
                                                                     word)

