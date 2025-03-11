from uuid import UUID

from pydantic import BaseModel


class IngredientSchema(BaseModel):
    id: UUID
    name: str
    quantity: float
    unit: str
