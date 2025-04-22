import pytest
from app import app

@pytest.fixture
def client():
    """
    Fixture to set up the Flask test client.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# TODO: write a test for the entire dataset route
def test_get_all_movies(client):

response = client.get('/movies')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0
    assert all('id' in movie for movie in response.json)
    assert all('title' in movie for movie in response.json)

    
# TODO: write a test for the movies between a certain release year range route

# TODO: write a test for the movie by id route

# TODO: write a test for the genres by movie route

# TODO: write a test for the movie by title route
