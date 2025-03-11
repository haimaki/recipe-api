import pytest
from pint import UnitRegistry
from sqlmodel import Session

from data.factories.recipeingredient import RecipeIngredientFactory
from data.models.enums import UnitSystem
from data.wrappers.ingredientunitwrapper import IngredientUnitWrapper


def test_convert_to_unit_converts_quantity_and_unit(session: Session) -> None:
    recipe_ingredient = RecipeIngredientFactory(quantity=1, unit="kg")
    wrapper = IngredientUnitWrapper(recipe_ingredient)
    wrapper.convert_to_unit("g")
    assert recipe_ingredient.quantity == 1000
    assert recipe_ingredient.unit == "gram"


def test_convert_to_unit_raises_error_if_invalid_conversion(session: Session) -> None:
    recipe_ingredient = RecipeIngredientFactory(unit="kg")
    wrapper = IngredientUnitWrapper(recipe_ingredient)
    with pytest.raises(ValueError, match="Cannot convert between kg and m"):
        wrapper.convert_to_unit("m")


def test_convert_to_unit_raises_error_if_invalid_unit(session: Session) -> None:
    recipe_ingredient = RecipeIngredientFactory()
    wrapper = IngredientUnitWrapper(recipe_ingredient)
    with pytest.raises(ValueError, match="Unit asdf is not recognized"):
        wrapper.convert_to_unit("asdf")


@pytest.mark.parametrize(
    ("unit", "system", "expected_unit"),
    [
        ("kilogram", UnitSystem.IMPERIAL, "pound"),
        ("pound", UnitSystem.METRIC, "kilogram"),
    ],
)
def test_convert_to_system_converts_to_base_units_for_mass(
    session: Session, unit: str, system: UnitSystem, expected_unit: str
) -> None:
    recipe_ingredient = RecipeIngredientFactory(quantity=1, unit=unit)
    wrapper = IngredientUnitWrapper(recipe_ingredient)
    wrapper.convert_to_system(system)

    ureg = UnitRegistry()
    expected_quantity = ureg.Quantity(1, unit)
    ureg.default_system = system
    expected_quantity = expected_quantity.to_base_units().magnitude
    assert recipe_ingredient.quantity == expected_quantity
