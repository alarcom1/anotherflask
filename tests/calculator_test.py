"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator

def tuple_list():
    """Arranging data for AAA testing"""
    return 1.0, 2

def test_calculator_add_method():
    """Testing the Calculator"""
    # this id using the calculator object add method

    ## Act for AAA testing
    result = Calculator.add(tuple_list())

    ## Assertion for AAA
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert Calculator.subtract(tuple_list()) == -3


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    assert Calculator.multiply(tuple_list()) == 2
