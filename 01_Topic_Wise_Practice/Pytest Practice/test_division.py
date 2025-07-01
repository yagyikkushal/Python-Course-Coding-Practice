# Write a function that divides two numbers.
# Then write pytest cases to:
#
# Check correct division
#
# Handle zero division using pytest.raises(ZeroDivisionError)

import pytest

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a/b

def test_divide():
    assert divide(2,2) == 1
    assert divide(4,2) == 2
    assert divide(48,12) == 4
    with pytest.raises(ZeroDivisionError):
        divide(2,0)