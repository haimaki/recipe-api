from data.models import RecipeIngredient


def adjust_portion_size(
    recipe_ingredients: list[RecipeIngredient], portion_size: float
) -> list[RecipeIngredient]:
    for ingredient in recipe_ingredients:
        ingredient.quantity = ingredient.quantity * portion_size
    return recipe_ingredients
