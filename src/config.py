import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("API_KEY")
username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
database = os.getenv("DATABASE_NAME")

DB_CONNECTION_STRING = f"postgresql://{username}:{password}@{host}:{port}/{database}"
