### 5. Testing in Flask

# Do your own research on how you can test your Flask application with Pytest. You can take a look at this snippet for inspiration:

### ```python

# test_app.py
import pytest
from app import app
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    # Test the GET /users endpoint
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == ["Alice", "Bob"] 

def test_create_user(client):
    # Test the POST /users endpoint with valid data
    response = client.post('/users', json={'name': 'Alice'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'Alice'

def test_create_user_without_name(client):
    # Test the POST /users endpoint without 'name'
    response = client.post('/users', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Name is required'}


# Step 1: Install Pytest
# Step 2: Structure Your Project
# /your_project
# ├── app.py              # Your Flask application
# ├── test_app.py         # Your test cases
# └── requirements.txt    # Your dependencies (optional)
# Step 3: Write Your Flask Application
# Step 4: Write Your Test Cases
# The test_client method is used to simulate HTTP requests during testing.
# < app.config['TESTING'] = True > : Set the app in testing mode
# Step 5: Run Your Tests

