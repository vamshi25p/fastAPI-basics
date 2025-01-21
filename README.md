# FastAPI Blog Project

This is a simple blog application built with **FastAPI** and **SQLAlchemy** for the backend and **PostgreSQL** as the database. The app allows users to create and manage blog posts with authentication and authorization.

## Features

- User registration and login (JWT authentication)
- Create, read, update, and delete blog posts
- PostgreSQL database integration
- API documentation using **Swagger UI** (`/docs`) and **ReDoc** (`/redoc`)

## Tech Stack

- **FastAPI**: Web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Relational database for storing user and blog data.
- **Pydantic**: Data validation for request and response models.
- **JWT**: Authentication via JSON Web Tokens.
- **Alembic**: For database migrations.
- **Uvicorn**: ASGI server for running FastAPI.

