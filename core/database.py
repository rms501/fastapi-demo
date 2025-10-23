from sqlmodel import create_engine, Session

from core.config import connection_string

engine = create_engine(connection_string, echo=True)

def get_session():
    with Session(engine) as session:
        yield session