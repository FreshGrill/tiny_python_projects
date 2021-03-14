#!/usr/bin/env python3
"""tests for hello.py"""

import os
import sys
from subprocess import getstatusoutput, getoutput, check_output
import subprocess

prg = './hello.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""

    # out = getoutput(prg)
    # assert out.strip() == 'Hello, World!'

    try:
        output = subprocess.check_output(['python3', prg])
    # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    assert output.decode('utf-8').strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        # rv, out = getstatusoutput(f'{prg} {flag}')
        try:
            out = subprocess.check_output(['python3', prg, flag])
        #  assert rv == 0
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)

        assert out.decode('utf-8').lower().startswith('usage')


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            try:
                out = subprocess.check_output(['python3', prg, option, val])
            # rv, out = getstatusoutput(f'{prg} {option} {val}')
            except subprocess.CalledProcessError as e:
                print("Command error: " + e.output)
                print("Command output: " + output)
                sys.exit(e.returncode)
            # assert rv == 0
            assert out.decode('utf-8').strip() == f'Hello, {val}!'
