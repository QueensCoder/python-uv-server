from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn


def main():
    print("Hello from python-uv-server!")


if __name__ == "__main__":
    main()
    # FastAPI app
    app = FastAPI()

    # Database configuration
    DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    # Dependency to get DB session
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Example route
    @app.get("/")
    def read_root():
        return {"message": "Welcome to the FastAPI server!"}

    # Run the FastAPI app

    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)
