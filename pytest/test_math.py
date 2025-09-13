def add (a,b):

    return a + b
def test0_add():

    assert add(2,4) == 6
def test1_add():
    assert add(-1,1) == 0
def test2_add():
    assert add(4,7) == 11
def test3_add():
    assert add (0,0) == 0