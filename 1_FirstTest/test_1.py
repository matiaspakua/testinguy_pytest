def test_equal():
# Passing Test 1
    assert 1 == 1

def test_greater():
# Passing Test 2
    assert 5 > 3

def test_lessthan_f1():
# Failing Test 1
# without message
    assert 3 < 2

def test_lessthan_f2():
# Failing Test 2
# with message
    assert 3 < 2, "3 is not less than 2"