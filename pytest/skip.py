import pytest

@pytest.mark.skip(reason="Not yet implemented")

def test_future_feature():
    pass

@pytest.mark.xfail(reason="kown bug")

def test_bug_case():
    assert 1/0 == 1