import pytest

from infotainment import set_volume

@pytest.mark.parametrize("level,expected",[
    (50, True),
    (0, True),
    (100, True),
    (-1, False),
    (120,False),
    (-34, True)

])

def test_set_volume(level,expected):

    assert set_volume(level) == expected