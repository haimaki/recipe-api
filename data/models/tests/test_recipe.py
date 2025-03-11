from sqlmodel import Session

from data.factories.recipe import RecipeFactory
from data.wrappers.ingredientunitwrapper import IngredientUnitWrapper


def test_recipe_wrapped_ingredients_returns_wrapped_ingredients(
    session: Session,
) -> None:
    recipe = RecipeFactory()
    wrapped_ingredients = recipe.wrapped_ingredients
    assert len(wrapped_ingredients) == 1
    assert isinstance(wrapped_ingredients[0], IngredientUnitWrapper)
