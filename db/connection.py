from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker


# Define the PostgreSQL database connection URL
load_dotenv()
db_url = os.environ.get("DB_URL")
# Create a database engine
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
