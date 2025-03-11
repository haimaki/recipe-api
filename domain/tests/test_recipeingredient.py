from sqlmodel import Session

from data.factories.recipeingredient import RecipeIngredientFactory
from domain.recipeingredient import adjust_portion_size


def test_adjust_portion_size_returns_adjusted_ingredients(session: Session) -> None:
    ingredients = RecipeIngredientFactory.create_batch(3, quantity=1)
    adjusted_ingredients = adjust_portion_size(ingredients, 2)
    for ingredient in adjusted_ingredients:
        assert ingredient.quantity == 2
