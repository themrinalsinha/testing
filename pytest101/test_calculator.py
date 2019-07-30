import pytest
from calculator import Calculator, CalculatorError

def test_add():
    calculator = Calculator()
    result     = calculator.add(2, 3)
    assert result == 5

def test_subtract():
    calculator = Calculator()
    result     = calculator.subtract(6, 1)
    assert result == 5

def test_multiply():
    calculator = Calculator()
    result     = calculator.multiply(5, 1)
    assert result == 5

def test_division():
    calculator = Calculator()
    result     = calculator.division(10, 2)
    assert result == 5

def test_add_weird_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.add('two', 3)
    # assert result == 5
