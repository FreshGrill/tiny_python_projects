#!/usr/bin/env python3
"""tests for howler.py"""

import os
import random
import re
import string
import subprocess
import sys

prg = "./howler.py"


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o or --outfile"""

    return "-o" if random.randint(0, 1) else "--outfile"


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
        # assert re.match("usage", out, re.IGNORECASE)
        output = ""
        try:
            output = subprocess.check_output(["python3", prg, flag])
            # print ("Command output: " + output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("Command error: " + e.output)
            print("Command output: " + output)
            sys.exit(e.returncode)
        # assert False,output.decode('utf-8').lower()
        assert re.match("usage", output.decode("utf-8"), re.IGNORECASE)


# --------------------------------------------------
def test_text_stdout():
    """Test STDIN/STDOUT"""

    # out = getoutput(f'{prg} "foo bar baz"')
    # assert out.strip() == 'FOO BAR BAZ'
    output = ""
    try:
        output = subprocess.check_output(["python3", prg, "foo bar baz"])
        # print ("Command output: " + output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Command error: " + e.output)
        print("Command output: " + output)
        sys.exit(e.returncode)
    # assert False,output.decode('utf-8').lower()
    assert output.decode("utf-8").strip() == "FOO BAR BAZ"


# --------------------------------------------------
def test_text_outfile():
    """Test STDIN/outfile"""

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        # out = getoutput(f'{prg} {out_flag()} {out_file} "foo bar baz"')
        out = (
            subprocess.check_output(
                ["python3", prg, out_flag(), out_file, "foo bar baz"]
            )
            .decode("utf-8")
            .strip()
        )
        assert out.strip() == ""
        assert os.path.isfile(out_file)
        text = open(out_file).read().rstrip()
        assert text == "FOO BAR BAZ"
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_file():
    """Test file in/out"""

    for expected_file in os.listdir("test-outs"):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join("../inputs", basename)
            # out = getoutput(f"{prg} {out_flag()} {out_file} {in_file}")
            out = (
                subprocess.check_output(
                    ["python3", prg, out_flag(), out_file, in_file]
                )
                .decode("utf-8")
                .strip()
            )
            assert out.strip() == ""
            produced = open(out_file).read().rstrip()
            expected = (
                open(os.path.join("test-outs", expected_file)).read().strip()
            )
            assert expected == produced
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)
