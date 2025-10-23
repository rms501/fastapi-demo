from typing import Sequence

from model.dao.student import Student
from repositories.student_repository import StudentRepository


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def get_students(self) -> Sequence[Student]:
        return self.repository.get_students()

    def get_student(self, student_id: int) -> Student:
        return self.repository.get_student(student_id)

    def create_student(self, student: Student) -> Student:
        return self.repository.create_student(student)

    def delete_student(self, student_id: int) -> None:
        return self.repository.delete_student(student_id)