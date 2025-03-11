from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from data.models import RecipeIngredient
    from data.wrappers.ingredientunitwrapper import IngredientUnitWrapper


class Recipe(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    recipe_ingredients: list["RecipeIngredient"] = Relationship(
        back_populates="recipe", cascade_delete=True
    )

    @property
    def wrapped_ingredients(self) -> list["IngredientUnitWrapper"]:
        from data.wrappers.ingredientunitwrapper import IngredientUnitWrapper

        return [
            IngredientUnitWrapper(ingredient) for ingredient in self.recipe_ingredients
        ]
