import pytest
import math_func

# def test_add():
#     assert math_func.add(7, 3) == 10

# def test_add_strings():
#     result = math_func.add('Hello ', 'world')
#     assert result == 'Hello world'

# def test_add_float():
#     result = math_func.add(10.5, 25.5)
#     assert result == 36

# OR

# def test__add():
#     assert math_func.add(7, 3) == 10
#     assert math_func.add('Hello ', 'world') == 'Hello world'
#     assert math_func.add(10.5, 25.5) == 36

# OR

@pytest.mark.parametrize('x, y, res', [
    (7, 3, 10),
    ('hello', ' world', 'hello world'),
    (10.5, 25.5, 36)
])
def test_add(x, y, res):
    assert math_func.add(x, y) == res