from typing import Sequence

from fastapi import APIRouter, Depends

from dependencies.student import get_student_service
from model.dao.student import Student
from model.dto.student import StudentResponse
from services.student_service import StudentService

router = APIRouter(prefix="/students")

@router.get("/", response_model=Sequence[StudentResponse])
def get_students(service: StudentService = Depends(get_student_service)):
    return service.get_students()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, service: StudentService = Depends(get_student_service)):
    return service.get_student(student_id)

@router.post("/", response_model=StudentResponse)
def post_student(student: Student, service: StudentService = Depends(get_student_service)):
    return service.create_student(student)

@router.delete("/{student_id}")
def delete_student(student_id: int, service: StudentService = Depends(get_student_service)):
    service.delete_student(student_id)