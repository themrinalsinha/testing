# Using pytest fixtures

from student_db import StudentDB
import pytest

# we have to pass scope here in order to avoide calling it twice.
@pytest.fixture(scope='module')
def db():
    print('-'*10, 'starting', '-'*10)
    db = StudentDB()
    db.connect('data.json')
    # return db
    # To have teardown in this method you remove return db to yield db
    yield db
    print('-'*10, 'ending', '-'*10)
    db.close()

# whatever you return in fixture will be passed as an argument in test functions.
def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
    scott_data = db.get_data('Mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'Mark'
    assert scott_data['result'] == 'fail'