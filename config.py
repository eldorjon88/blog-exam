import os
from dotenv import load_dotenv

load_dotenv()

# Config nomli class orqali qiling



class Config:
     DATABASE_URL = os.getenv(
    "DATABASE_URL",
     "postgresql://postgres:password@localhost/blog_db"
     )