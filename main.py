from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from api.v1 import student_controller, health_controller
from core.exceptions import StudentNotFoundError

app = FastAPI()
app.include_router(student_controller.router)
app.include_router(health_controller.router)

@app.exception_handler(SQLAlchemyError)
async def sql_alchemy_error_exception_handler(request: Request, exception: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={"message": "SQL Error occurred."}
    )

@app.exception_handler(StudentNotFoundError)
async def student_not_found_exception_handler(request: Request, exception: StudentNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"Student: {request.path_params.get('student_id')}, not found."},
    )