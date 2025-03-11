from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from data.models.enums import UnitSystem
from domain.recipe import get_all_recipes, get_recipe_by_id
from domain.recipeingredient import adjust_portion_size
from interfaces.schemas.ingredientschema import IngredientSchema
from interfaces.schemas.recipeschema import RecipeSchema

router = APIRouter()


@router.get("/", status_code=HTTP_200_OK)
def list_recipes() -> list[RecipeSchema]:
    return [RecipeSchema.model_validate(recipe) for recipe in get_all_recipes()]


@router.get("/{recipe_id}/ingredients", status_code=HTTP_200_OK)
def get_recipe_ingredient_list(
    recipe_id: UUID,
    portion_multiplier: Annotated[float, Query(gt=0)] | None = None,
    unit_system: UnitSystem | None = None,
) -> list[IngredientSchema]:
    if not (recipe := get_recipe_by_id(recipe_id)):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"Recipe {recipe_id} not found"
        )

    if portion_multiplier:
        recipe.recipe_ingredients = adjust_portion_size(
            recipe.recipe_ingredients, portion_multiplier
        )

    if unit_system:
        for wrapped in recipe.wrapped_ingredients:
            wrapped.convert_to_system(unit_system)

    return [
        IngredientSchema(
            id=ri.id, name=ri.ingredient.name, quantity=ri.quantity, unit=ri.unit
        )
        for ri in recipe.recipe_ingredients
    ]
