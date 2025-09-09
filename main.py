def get_weather(temp):

    if temp > 20:
        return "hot"
    else:
        return "cold"
    
def test1():

    assert get_weather(21) == "hot"

def test2():

    assert get_weather(21) == "cold"

def test3():

    assert get_weather(10) == "cold"

