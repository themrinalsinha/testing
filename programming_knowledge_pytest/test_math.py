import pytest
import math_func

def test_add():
    assert math_func.add(7, 3) == 10

def test_add_strings():
    result = math_func.add('Hello ', 'world')
    assert result == 'Hello world'

def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36