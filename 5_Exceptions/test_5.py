import sys

import pytest

import pytest

def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

def test_passes_without_info():
    with pytest.raises(Exception):
        x = 1 / 0

def test_fails():
    with pytest.raises(Exception) as e_info:
        x = 1 / 1

def test_fails_without_info():
    with pytest.raises(Exception):
        x = 1 / 1

