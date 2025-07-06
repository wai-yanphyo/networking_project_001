import pytest
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page returns 200 and correct content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Azure Automated Deployment Success!" in response.data
    assert b"🚀" in response.data

def test_home_page_content_type(client):
    """Test the home page returns correct content type."""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

def test_404_error(client):
    """Test 404 error for non-existent routes."""
    response = client.get('/nonexistent')
    assert response.status_code == 404