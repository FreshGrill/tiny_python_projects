#!/usr/bin/env python3
"""tests for picnic.py"""

import os
import subprocess
import sys

prg = "./picnic.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        # out = getoutput(f'{prg} {flag}')
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
def test_one():
    """one item"""

    # out = getoutput(f'{prg} chips')
    # assert out.strip() == 'You are bringing chips.'
    output = ""
    try:
        output = subprocess.check_output(["python3", prg, "chips"])
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    assert output.decode("utf-8").strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """two items"""

    # out = getoutput(f'{prg} soda "french fries"')
    # assert out.strip() == "You are bringing soda and french fries."
    output = ""
    try:
        output = subprocess.check_output(["python3", prg, "soda", "french fries"])
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    assert output.decode("utf-8").strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    # arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    # out = getoutput(f"{prg} {arg}")
    expected = "You are bringing potato chips, coleslaw, cupcakes and French silk pie."
    # assert out.strip() == expected
    output = ""
    try:
        output = subprocess.check_output(
            [
                "python3",
                prg,
                "potato chips",
                "coleslaw",
                "cupcakes",
                "French silk pie",
            ]
        )
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    assert output.decode("utf-8").strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    # out = getoutput(f"{prg} -s soda candy")
    # assert out.strip() == "You are bringing candy and soda."
    output = ""
    try:
        output = subprocess.check_output(["python3", prg, "-s", "soda", "candy"])
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    assert output.decode("utf-8").strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    # arg = "bananas apples dates cherries"
    # out = getoutput(f"{prg} {arg} --sorted")
    expected = "You are bringing apples, bananas, cherries and dates."
    # assert out.strip() == expected
    output = ""
    try:
        output = subprocess.check_output(
            ["python3", prg, "-s", "bananas", "apples", "dates", "cherries"]
        )
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    assert output.decode("utf-8").strip() == expected
