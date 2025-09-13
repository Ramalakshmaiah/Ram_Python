import pytest

@pytest.fixture

def sample_data():
    return {"name":"Ram","age":35}

def test_user_name(sample_data):
    assert sample_data["name"] == "Ram"
def test_user_age(sample_data):
    assert sample_data["age"] == 35
    