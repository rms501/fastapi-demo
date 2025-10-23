from fastapi import Depends
from sqlmodel import Session

from core.database import get_session
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


def get_student_repository(session: Session = Depends(get_session)) -> StudentRepository:
    return StudentRepository(session)

def get_student_service(repo: StudentRepository = Depends(get_student_repository)) -> StudentService:
    return StudentService(repo)