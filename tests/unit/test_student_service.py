import pytest

from model.dao.student import Student
from services.student_service import StudentService


@pytest.fixture
def mock_repository(mocker):
    return mocker.Mock()

@pytest.fixture
def service(mock_repository):
    return StudentService(mock_repository)

def test_get_students_returns_students(service, mock_repository):
    students = [
        Student(id=1, first_name="John", last_name="Doe", age=20, score=90),
        Student(id=2, first_name="Jane", last_name="Smith", age=22, score=95),
    ]
    mock_repository.get_students.return_value = students

    result = service.get_students()

    assert result == students
    mock_repository.get_students.assert_called_once_with()

def test_get_student_returns_student(service, mock_repository):
    student = Student(id=1, first_name="John", last_name="Doe", age=20, score=90)
    mock_repository.get_student.return_value = student

    result = service.get_student(1)

    assert result == student
    mock_repository.get_student.assert_called_once_with(1)

def test_create_student_creates_student(service, mock_repository):
    student = Student(first_name="John", last_name="Doe", age=20, score=90)
    created_student = Student(id=1, first_name="John", last_name="Doe", age=20, score=90)

    mock_repository.create_student.return_value = created_student

    result = service.create_student(student)

    assert result == created_student
    mock_repository.create_student.assert_called_once_with(student)

def test_delete_student_deletes_student(service, mock_repository):
    service.delete_student(1)

    mock_repository.delete_student.assert_called_once_with(1)