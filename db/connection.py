from sqlalchemy import create_engine
import os

# Define the PostgreSQL database connection URL
db_url = os.environ.get("DB_URL")
# Create a database engine
engine = create_engine(db_url)
