from config.env_config import DATABASE_URL
from sqlalchemy import create_engine, text


def connect_database():
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("Connected to database", conn)
    return conn
