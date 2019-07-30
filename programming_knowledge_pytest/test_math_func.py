import math_func
import pytest

# @pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7, 1) == 8
    assert math_func.add(7)    == 9

# @pytest.mark.number
def test_product():
    assert math_func.product(7, 10) == 70
    assert math_func.product(7)     == 14
    # assert math_func.product(7)     == 12

# @pytest.mark.strings
def test_add_string():
    result = math_func.add('hello ', 'world')
    assert result == 'hello world'
    assert type(result) is str
    assert 'helio' not in result

@pytest.mark.skip(reason='just testing the skip function')
def test_product_string():
    assert math_func.product('hello ', 3) == 'hello hello hello '
    result = math_func.product('hello ')
    assert result == 'hello hello '
    assert type(result) is str
    assert 'hello' in result


# # # Different ways of running scripts
# $ pytest
# $ pytest -v
# $ pytest sample_testing.py -v          # with different file name
# $ pytest test_math_func.py::test_add   # to run specific function

# If you just want to run functions with add
# $ pytest -v -k "add"                   # function havig add in name
# $ pytest -v -k "add or string"         # function having add or string in name
# $ pytest -v -k "add and string"        # function having add and string in name


# Running tests with marker ('-m') option
# $ pytest -v -m number
# $ pytest -v -m strings

# Running tests with ('-x') option
# It'll exit with first error

# if you want to supress the stack tract means just show if function passed or not
# $ pytest -v --tb=no

# maximum fail -> $ pytest -v --maxfail=2

# skipping a particular function for test
# if you want to show the reason for skips in verbose mode on the terminal
# you can pass -rsx to report skipped tests
# $ pytest -v -rsx