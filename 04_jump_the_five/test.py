#!/usr/bin/env python3
"""tests for jump.py"""

import os
import subprocess
import sys


prg = "./jump.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        # rv, out = getstatusoutput(f'{prg} {flag}')
        # assert rv == 0
        # assert out.lower().startswith('usage')

        output = ""
        try:
            output = subprocess.check_output(["python3", prg, flag])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        # assert False,output.decode('utf-8').lower()
        assert output.decode("utf-8").lower().strip().startswith("usage")


# --------------------------------------------------
def test_01():
    """test"""

    # rv, out = getstatusoutput(f'{prg} 123-456-7890')
    # assert rv == 0
    # assert out == '987-604-3215'
    output = ""
    try:
        output = subprocess.check_output(["python3", prg, "123-456-7890"])
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    # assert False,output.decode('utf-8').lower()
    assert output.decode("utf-8") == "987-604-3215"


# --------------------------------------------------
def test_02():
    """test"""

    # rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    # assert rv == 0
    # assert out.rstrip() == 'That number to call is 512-340-6789.'
    output = ""
    try:
        output = subprocess.check_output(
            ["python3", prg, "That number to call is 098-765-4321."]
        )
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    # assert False,output.decode('utf-8').lower()
    assert (
        output.decode("utf-8").rstrip()
        == "That number to call is 512-340-6789."
    )
