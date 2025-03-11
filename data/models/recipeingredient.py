from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from data.models import Ingredient, Recipe


class RecipeIngredient(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    recipe_id: UUID = Field(foreign_key="recipe.id")
    recipe: "Recipe" = Relationship(back_populates="recipe_ingredients")
    ingredient_id: UUID = Field(foreign_key="ingredient.id")
    ingredient: "Ingredient" = Relationship(back_populates="recipe_ingredients")
    quantity: float
    unit: str
