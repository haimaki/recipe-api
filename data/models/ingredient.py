from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from data.models import RecipeIngredient


class Ingredient(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    recipe_ingredients: list["RecipeIngredient"] = Relationship(
        back_populates="ingredient", cascade_delete=True
    )
    # Could extend this at a later point with ingredient type, brands etc.
