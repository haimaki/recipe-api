from sqlmodel import SQLModel

from data import models  # noqa: F401
from domain.db import get_engine

if __name__ == "__main__":  # pragma: no cover
    SQLModel.metadata.create_all(get_engine())
