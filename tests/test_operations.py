from src.math_operations import add , multiply


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_multiply():
    assert multiply(5,3)==15
    assert multiply(4,6)==33