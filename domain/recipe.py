from uuid import UUID

from sqlmodel import select

from data.models import Recipe
from domain.db import get_session


def get_all_recipes() -> list[Recipe]:
    with get_session() as session:
        return list(session.exec(select(Recipe)).all())


def get_recipe_by_id(recipe_id: UUID) -> Recipe | None:
    with get_session() as session:
        return session.get(Recipe, recipe_id)
