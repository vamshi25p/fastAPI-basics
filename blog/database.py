from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define Base
Base = declarative_base()

# Set up PostgreSQL connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/mydatabase"

# Set up SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db(): 
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()
