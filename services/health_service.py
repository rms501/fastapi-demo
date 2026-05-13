from sqlmodel import Session
from sqlalchemy import text


class HealthService:

    def __init__(self, session: Session):
        self.session = session

    def check_health(self):
        return self.session.exec(text("SELECT 1")).scalar_one() == 1