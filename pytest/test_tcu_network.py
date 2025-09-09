import pytest
from tcu_network import is_valid_network

@pytest.mark.parametrize("mode,expected", [
        ("5G", True),
        ("LTE",True),
        ("2G", False),
        ("3G", False)

])

def test_network_registration(mode,expected):
    assert is_valid_network(mode) == expected