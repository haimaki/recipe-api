from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RecipeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
