from pint import DimensionalityError, UndefinedUnitError, UnitRegistry

from data.models import RecipeIngredient
from data.models.enums import UnitSystem

ureg = UnitRegistry()


class IngredientUnitWrapper:
    def __init__(self, recipe_ingredient: RecipeIngredient) -> None:
        self.recipe_ingredient = recipe_ingredient

    def convert_to_unit(self, unit: str) -> None:
        quantity = ureg.Quantity(
            self.recipe_ingredient.quantity, self.recipe_ingredient.unit
        )
        try:
            conversion_unit = ureg(unit)
            converted_quantity = quantity.to(conversion_unit)
            self.recipe_ingredient.quantity = converted_quantity.magnitude
            self.recipe_ingredient.unit = str(converted_quantity.units)
        except UndefinedUnitError as e:
            msg = f"Unit {unit} is not recognized"
            raise ValueError(msg) from e
        except DimensionalityError as e:
            msg = f"Cannot convert between {self.recipe_ingredient.unit} and {unit}"
            raise ValueError(msg) from e

    def convert_to_system(self, system: UnitSystem) -> None:
        quantity = ureg.Quantity(
            self.recipe_ingredient.quantity, self.recipe_ingredient.unit
        )
        ureg.default_system = system
        converted_quantity = quantity.to_base_units()
        self.recipe_ingredient.quantity = converted_quantity.magnitude
        self.recipe_ingredient.unit = str(converted_quantity.units)
