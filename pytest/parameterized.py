import pytest

@pytest.mark.parametrize("a,b,result",[
    
    (2,3,5),
    (4,6,10),
    (-4,2,2),
    (10,-8,2)

])

def test_addition(a,b,result):
    assert a+b == result