import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7, 1) == 8
    assert math_func.add(7)    == 9

def test_product():
    assert math_func.product(7, 10) == 70
    assert math_func.product(7)     == 14
    # assert math_func.product(7)     == 12

def test_add_string():
    result = math_func.add('hello ', 'world')
    assert result == 'hello world'
    assert type(result) is str
    assert 'helio' not in result

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