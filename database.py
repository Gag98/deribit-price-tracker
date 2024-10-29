import psycopg2
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
DB_NAME = "crypto_db"

def create_database_if_not_exists():
    db_url_no_db = DATABASE_URL.replace("postgresql+asyncpg", "postgresql").rsplit('/', 1)[0] + "/postgres"
    conn = psycopg2.connect(db_url_no_db)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
    cursor.close()
    conn.close()

create_database_if_not_exists()

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
metadata = MetaData()

prices = Table(
    "prices",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("ticker", String, index=True),
    Column("price", Float),
    Column("timestamp", Integer)
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
