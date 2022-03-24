"""testing the calculator"""
# from specifies the namespace
from calculator.calculations import Addition, Subtraction, Multiplication


def test_calculation_multiplication_instance():
    """testing the Calculator Multiplication"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)

def test_calculation_subtraction_instance():
    """testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)

def test_calculation_addition_instance():
    """testing the Calculator Addition"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)

def test_calculation_add_get_result_method():
    """testing the Calculator"""
    # this is show using the calculator object and method
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3
