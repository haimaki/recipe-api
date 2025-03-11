from uuid import uuid4

from sqlmodel import Session

from data.factories.recipe import RecipeFactory
from data.models import Recipe
from domain.recipe import get_all_recipes, get_recipe_by_id


def test_get_all_recipes_returns_recipes(session: Session) -> None:
    RecipeFactory.create_batch(3)
    recipes = get_all_recipes()
    assert len(recipes) == 3
    assert all(isinstance(recipe, Recipe) for recipe in recipes)


def test_get_all_recipes_returns_empty_list_if_no_recipes(session: Session) -> None:
    recipes = get_all_recipes()
    assert not recipes


def test_get_recipe_by_id_returns_recipe(session: Session) -> None:
    recipe = RecipeFactory()
    result = get_recipe_by_id(recipe.id)
    assert result
    assert result.id == recipe.id


def test_get_recipe_by_id_returns_none_if_not_found(session: Session) -> None:
    result = get_recipe_by_id(uuid4())
    assert not result
