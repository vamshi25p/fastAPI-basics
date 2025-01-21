import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from blog.models import User, Blog  # Import models from models.py
from blog.database import Base, SessionLocal  # Import Base and SessionLocal from database.py

# Connect to SQLite database
sqlite_conn = sqlite3.connect('./blog.db')
sqlite_cursor = sqlite_conn.cursor()

# Fetch data from SQLite
sqlite_cursor.execute("SELECT * FROM users")
users = sqlite_cursor.fetchall()

sqlite_cursor.execute("SELECT * FROM blogs")
blogs = sqlite_cursor.fetchall()

# Connect to PostgreSQL database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/mydatabase"  # Update as needed

# Using the engine you defined earlier for PostgreSQL connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create all tables in PostgreSQL (if not already created)
Base.metadata.create_all(bind=engine)

# Use the sessionmaker you defined earlier to connect to PostgreSQL
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = SessionLocal()

try:
    # Insert Users into PostgreSQL
    for user in users:
        new_user = User(id=user[0], name=user[1], email=user[2], password=user[3])
        session.add(new_user)

    # Commit users to ensure they have valid IDs before inserting blogs
    session.commit()

    # Insert Blogs into PostgreSQL
    for blog in blogs:
        # Find the corresponding user for the foreign key
        user_id = blog[3]  # Assuming user_id is the 4th element in the blog tuple
        new_blog = Blog(id=blog[0], title=blog[1], body=blog[2], user_id=user_id)
        session.add(new_blog)

    # Commit all blog data
    session.commit()

    print("Migration completed successfully!")

except Exception as e:
    session.rollback()  # Rollback if any error occurs
    print(f"Error during migration: {e}")

finally:
    # Close SQLite and PostgreSQL sessions
    sqlite_conn.close()
    session.close()

# Optional: Define get_db() function to use PostgreSQL session in FastAPI
def get_db(): 
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()
