from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from dependencies.health import get_health_service
from services.health_service import HealthService

router = APIRouter(prefix="/health")

@router.get("/")
def health_check(service: HealthService = Depends(get_health_service)):
    failure_response = JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={ "status": "degraded", "database": "unhealthy" }
    )

    try:
        response = failure_response

        if service.check_health():
            response =  JSONResponse(
                status_code=status.HTTP_200_OK,
                content={ "status": "ok", "database": "ok" }
            )

        return response

    except SQLAlchemyError:
        return failure_response