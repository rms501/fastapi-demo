from fastapi.params import Depends
from sqlmodel import Session

from core.database import get_session
from services.health_service import HealthService


def get_health_service(session: Session = Depends(get_session)) -> HealthService:
    return HealthService(session)