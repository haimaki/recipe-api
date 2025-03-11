from uuid import uuid4

from factory import LazyFunction
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker

from data.models import Ingredient
from domain.db import get_session


class IngredientFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Ingredient
        sqlalchemy_session_factory = get_session

    id = LazyFunction(uuid4)
    name = Faker().word()
