import os

connection_string = os.getenv("DATABASE_URL", "postgresql://admin:admin@db:5432/mydb")
