from unittest.mock import MagicMock, PropertyMock, patch
from uuid import uuid4

from fastapi.testclient import TestClient
from sqlmodel import Session

from data.factories.recipe import RecipeFactory
from interfaces.api import app

client = TestClient(app)


@patch("interfaces.rest_api.routers.recipe.get_all_recipes")
def test_list_recipes_returns_recipe_schemas(
    mock_get_recipes: MagicMock, session: Session
) -> None:
    recipes = RecipeFactory.create_batch(3)
    mock_get_recipes.return_value = recipes
    response = client.get("/recipe/")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json() == [{"id": str(r.id), "title": r.title} for r in recipes]


@patch("interfaces.rest_api.routers.recipe.get_recipe_by_id")
def test_get_recipe_ingredient_list_returns_ingredient_list_schema(
    mock_get_recipe_by_id: MagicMock, session: Session
) -> None:
    recipe = RecipeFactory()
    mock_get_recipe_by_id.return_value = recipe
    response = client.get(f"/recipe/{recipe.id}/ingredients")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": str(ri.id),
            "name": ri.ingredient.name,
            "quantity": ri.quantity,
            "unit": ri.unit,
        }
        for ri in recipe.recipe_ingredients
    ]


@patch("interfaces.rest_api.routers.recipe.get_recipe_by_id")
def test_get_recipe_ingredient_list_raises_error_for_invalid_recipe_id(
    mock_get_recipe_by_id: MagicMock, session: Session
) -> None:
    mock_get_recipe_by_id.return_value = None
    recipe_id = uuid4()
    response = client.get(f"/recipe/{recipe_id}/ingredients")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Recipe {recipe_id} not found"}


@patch("interfaces.rest_api.routers.recipe.get_recipe_by_id")
@patch("interfaces.rest_api.routers.recipe.adjust_portion_size")
def test_get_recipe_ingredient_list_calls_portion_size(
    mock_adjust_portion_size: MagicMock,
    mock_get_recipe_by_id: MagicMock,
    session: Session,
) -> None:
    recipe = RecipeFactory()
    ingredients = recipe.recipe_ingredients
    mock_get_recipe_by_id.return_value = recipe
    response = client.get(f"/recipe/{recipe.id}/ingredients?portion_multiplier=2")
    assert response.status_code == 200
    mock_adjust_portion_size.assert_called_once_with(ingredients, 2.0)


@patch("interfaces.rest_api.routers.recipe.get_recipe_by_id")
def test_get_recipe_ingredient_list_calls_convert_to_system(
    mock_get_recipe_by_id: MagicMock, session: Session
) -> None:
    recipe = RecipeFactory()
    wrapped_ingredient = MagicMock()
    mock_wrapped_ingredients = PropertyMock(return_value=[wrapped_ingredient])
    type(recipe).wrapped_ingredients = mock_wrapped_ingredients
    mock_get_recipe_by_id.return_value = recipe

    response = client.get(f"/recipe/{recipe.id}/ingredients?unit_system=mks")
    assert response.status_code == 200
    wrapped_ingredient.convert_to_system.assert_called_once_with("mks")
