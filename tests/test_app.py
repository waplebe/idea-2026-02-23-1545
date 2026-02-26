import pytest
from app import app, db
from flask import url_for

@pytest.fixture
def app_instance():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    db.init_app(app)
    return app

def test_get_tasks(app_instance):
    with app_instance.test_request_context():
        db.drop_all()
        db.create_all()
        task1 = Task(title='Test Task 1', description='Test Description 1')
        db.session.add(task1)
        db.session.commit()

        tasks = app_instance.get_route('/tasks').execute()
        assert isinstance(tasks, list)
        assert len(tasks) == 1
        assert tasks[0]['title'] == 'Test Task 1'

def test_get_task(app_instance):
    with app_instance.test_request_context():
        db.drop_all()
        db.create_all()
        task1 = Task(title='Test Task 1', description='Test Description 1')
        db.session.add(task1)
        db.session.commit()

        task = app_instance.get_route('/tasks/1').execute()
        assert isinstance(task, dict)
        assert task['title'] == 'Test Task 1'
        assert task['description'] == 'Test Description 1'

def test_create_task(app_instance):
    with app_instance.test_request_context():
        db.drop_all()
        db.create_all()
        data = {'title': 'New Task', 'description': 'New Description'}
        response = app_instance.get_route('/tasks', methods=['POST']).execute(data=request.json)
        assert response['title'] == 'New Task'
        assert response['description'] == 'New Description'
        assert len(Task.query.all()) == 1

def test_update_task(app_instance):
    with app_instance.test_request_context():
        db.drop_all()
        db.create_all()
        task1 = Task(title='Original Task', description='Original Description')
        db.session.add(task1)
        db.session.commit()

        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = app_instance.get_route('/tasks/1', methods=['PUT']).execute(data=request.json)
        assert response['title'] == 'Updated Task'
        assert response['description'] == 'Updated Description'
        assert task1.title == 'Updated Task'
        assert task1.description == 'Updated Description'

def test_delete_task(app_instance):
    with app_instance.test_request_context():
        db.drop_all()
        db.create_all()
        task1 = Task(title='Delete Task', description='Delete Description')
        db.session.add(task1)
        db.session.commit()

        response = app_instance.get_route('/tasks/1', methods=['DELETE']).execute()
        assert response == ''
        assert len(Task.query.all()) == 0