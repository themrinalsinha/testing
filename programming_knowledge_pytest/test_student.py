from student_db import StudentDB
import pytest

# Using setup and teardown method
db = None
def setup_module(module):
    print('\n', '-'*10, ' setup module ', '-'*10)
    global db
    db = StudentDB()
    db.connect('data.json')

def teardown_module(module):
    print('\n', '-'*10, ' teardown module ', '-'*10)
    db.close()

def test_scott_data():
    # db = StudentDB()
    # db.connect('data.json')
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data():
    # db = StudentDB()
    # db.connect('data.json')
    scott_data = db.get_data('Mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'Mark'
    assert scott_data['result'] == 'fail'

# as you can see above, there is alot of code repeation here,
# we are also initializing db alot of times, which is high resource intensive

# In order to first solve it, we'll use setup and tear down method.
