import pytest
from app import app, db
from unittest.mock import patch

@pytest.fixture
def test_db(request):
    db.drop_all()
    db.create_all()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    yield app
    db.session.remove()

@patch('app.load_dotenv')
def test_get_tasks(mock_load_dotenv):
    mock_load_dotenv.return_value = None
    response = app.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@patch('app.load_dotenv')
def test_get_task(mock_load_dotenv):
    Task.query.get_or_404.return_value = Task(id=1, title='Test Task', description='Test Description')
    response = app.get('/tasks/1')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@patch('app.load_dotenv')
def test_create_task(mock_load_dotenv):
    data = {'title': 'Test Task', 'description': 'Test Description'}
    request_data = request.get_json()
    assert request_data == data
    response = app.post('/tasks', data=data)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)

@patch('app.load_dotenv')
def test_update_task(mock_load_dotenv):
    Task.query.get_or_404.return_value = Task(id=1, title='Old Task', description='Old Description')
    data = {'title': 'New Task', 'description': 'New Description'}
    request_data = request.get_json()
    assert request_data == data
    response = app.put('/tasks/1', data=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@patch('app.load_dotenv')
def test_delete_task(mock_load_dotenv):
    Task.query.get_or_404.return_value = Task(id=1, title='Test Task', description='Test Description')
    response = app.delete('/tasks/1')
    assert response.status_code == 204