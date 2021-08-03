import sys

import pytest

def has_number(input_string):
    return any(char.isdigit() for char in input_string)

def test_has_number_valid():
# Single test with valid input
    assert has_number("I have 1 dollar")

def test_has_number_invalid():
# Single test with invalid input
    assert not has_number("I have one dollar")

@pytest.mark.skip()
@pytest.mark.parametrize("input_string, expected", [
    ("1", True),
    ("a1", True),
    ("Bob", False),
    ("I have 1 dollar", True),
    ("Do I have one dollar?", False),
    ("1abc", True),
    ("", False),
])
def test_has_number(input_string : str, expected: bool):
# Single test with parametrize
    assert has_number(input_string) == expected, f"Test failed for input string '{input_string}'"

