import os

from dotenv import load_dotenv
from sqlalchemy import Engine
from sqlmodel import Session, create_engine

load_dotenv()
pg_connection_string = os.getenv("POSTGRES_CONNECTION_STRING")
if not pg_connection_string:  # pragma: no cover
    msg = "POSTGRES_CONNECTION_STRING is not set"
    raise ValueError(msg)


def get_engine() -> Engine:
    return create_engine(pg_connection_string)


def get_session() -> Session:
    return Session(get_engine())
