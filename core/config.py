import os
from typing import Any, Dict, List, Optional, Union
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

from pydantic import AnyHttpUrl, validator
from sqlalchemy.engine import create_engine

load_dotenv()

class Settings(BaseSettings):
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_port: int = os.getenv("DB_PORT")
    db_name: str = os.getenv("DB_NAME")
    db_url: str = os.getenv("DATABASE_URL")
    
settings = Settings()
