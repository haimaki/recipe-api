from typing import Generator

import pytest
from pytest_mock import MockerFixture
from sqlalchemy import StaticPool, create_engine, Engine
from sqlmodel import Session, SQLModel

from data import models  # noqa


@pytest.fixture
def sqlite_in_memory_db_engine() -> Engine:
    return create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )


@pytest.fixture
def session(
    mocker: MockerFixture, sqlite_in_memory_db_engine: Engine
) -> Generator[Session, None, None]:
    SQLModel.metadata.create_all(sqlite_in_memory_db_engine)
    with Session(sqlite_in_memory_db_engine) as session:
        mocker.patch("domain.db.Session", return_value=session)
        yield session
