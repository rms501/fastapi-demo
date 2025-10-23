from typing import Sequence

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select, Session

from core.exceptions import StudentNotFoundError
from model.dao.student import Student


class StudentRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_students(self) -> Sequence[Student]:
        return self.session.exec(select(Student)).all()

    def get_student(self, student_id: int) -> Student:
        student = self.session.exec(select(Student).where(Student.id == student_id)).first()
        if not student:
            raise StudentNotFoundError()
        return student

    def create_student(self, student: Student) -> Student:
        try:
            self.session.add(student)
            self.session.commit()
            self.session.refresh(student)
            return student
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def delete_student(self, student_id: int) -> None:
        try:
            student = self.session.exec(select(Student).where(Student.id == student_id)).first()
            if not student:
                raise StudentNotFoundError()
            self.session.delete(student)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise