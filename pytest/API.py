import pytest
import requests

@pytest.mark.parametrize("endpoint", [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2"
])
def test_api_response(endpoint):
    response = requests.get(endpoint)
    assert response.status_code == 200
    assert "userId" in response.json()