import sys

import pytest

@pytest.mark.skip(reason = "Skipping this test for Demo")
def test_skip():
# Skip tests
    assert 1 == 1

@pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
def test_skipif():
# Skip test when executed on non linux envs
    assert sys.platform == "linux"

@pytest.mark.xfail(reason = "Expected failure due to open defect ID-101")
def test_xfail():
# A Test marked as expected failure
    assert 4 < 5

@pytest.mark.xfail(sys.platform == "win32",reason = "This test is expected fail in non Linux")
def test_xfail_with_condition():
# A Test marked as expected failure with condition
    assert sys.platform == "linux"
