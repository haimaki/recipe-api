from uuid import uuid4

from factory import LazyFunction, RelatedFactory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker

from data.factories.recipeingredient import RecipeIngredientFactory
from data.models import Recipe
from domain.db import get_session


class RecipeFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Recipe
        sqlalchemy_session_factory = get_session

    id = LazyFunction(uuid4)
    title = Faker().word()
    ingredients_list = RelatedFactory(RecipeIngredientFactory, "recipe")
