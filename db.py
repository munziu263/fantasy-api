# Core
from dataclasses import dataclass
import toml

# Packages
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# --- CONFIG
@dataclass
class Config:
    user: str
    password: str
    host: str
    name: str
    port: int


secrets = toml.load("secrets.toml")["db"]
config = Config(**secrets)
db_url = f"postgresql+psycopg2://{config.user}:{config.password}@{config.host}:{config.port}/{config.name}"

# --- END CONFIG


engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    """Session generator for FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
