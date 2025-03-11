import random
from uuid import uuid4

from factory import LazyFunction, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
from pint import UnitRegistry

from data.factories.ingredient import IngredientFactory
from data.models import RecipeIngredient
from domain.db import get_session

ureg = UnitRegistry()


class RecipeIngredientFactory(SQLAlchemyModelFactory):
    class Meta:
        model = RecipeIngredient
        sqlalchemy_session_factory = get_session

    id = LazyFunction(uuid4)
    recipe = SubFactory("data.factories.recipe.RecipeFactory")
    ingredient = SubFactory(IngredientFactory)
    quantity = Faker().pyfloat(positive=True)
    unit = LazyFunction(lambda: str(random.choice(list(ureg))))
