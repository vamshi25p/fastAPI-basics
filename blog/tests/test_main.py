from fastapi.testclient import TestClient
from blog.main import app
from blog.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from blog.models import Base
from blog.authtoken import create_access_token  # Import your JWT token creation function
from datetime import timedelta

# Setup for SQLite in-memory database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database

# Creating a test engine and session local
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency for tests to use the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the dependency in the FastAPI app
app.dependency_overrides[get_db] = override_get_db

# Create tables in the test database
Base.metadata.create_all(bind=engine)

# Create the test client for sending requests to the FastAPI app
client = TestClient(app)

# Helper function to create a test user and return a JWT token
def create_test_user():
    user_data = {
        "name": "Test User 1",
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = client.post("/user", json=user_data)
    return response.json()


def test_create_user():
    response = client.post(
        "/user",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpassword"
        }
    )
    
    # Check response and test status
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"
    assert response.json()["email"] == "test@example.com", "Email doesn't match the expected value"
    
    # This will be automatically displayed by pytest
    print("Test 'test_create_user' passed")
