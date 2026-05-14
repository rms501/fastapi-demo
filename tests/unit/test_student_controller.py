import pytest
from fastapi.testclient import TestClient

from main import app
from dependencies.student import get_student_service
from model.dao.student import Student

@pytest.fixture
def mock_student_service(mocker):
    return mocker.Mock()

@pytest.fixture
def client(mock_student_service):
    app.dependency_overrides[get_student_service] = lambda: mock_student_service

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

def test_get_students_returns_200(client, mock_student_service):
    mock_student_service.get_students.return_value = [
        Student(id=1, first_name="John", last_name="Doe", age=20, score=90),
        Student(id=2, first_name="Jane", last_name="Smith", age=22, score=95),
    ]

    response = client.get("/students/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "first_name": "John", "last_name": "Doe", "age": 20, "score": 90},
        {"id": 2, "first_name": "Jane", "last_name": "Smith", "age": 22, "score": 95},
    ]

    mock_student_service.get_students.assert_called_once_with()

def test_get_student_returns_200(client, mock_student_service):
    mock_student_service.get_student.return_value = Student(
        id=1,
        first_name="John",
        last_name="Doe",
        age=20,
        score=90,
    )

    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 20,
        "score": 90,
    }

    mock_student_service.get_student.assert_called_once_with(1)

def test_post_student_returns_200(client, mock_student_service):
    mock_student_service.create_student.return_value = Student(
        id=1,
        first_name="John",
        last_name="Doe",
        age=20,
        score=90,
    )

    response = client.post(
        "/students/",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "age": 20,
            "score": 90,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 20,
        "score": 90,
    }

    mock_student_service.create_student.assert_called_once()

def test_delete_student_returns_200(client, mock_student_service):
    response = client.delete("/students/1")

    assert response.status_code == 200
    mock_student_service.delete_student.assert_called_once_with(1)