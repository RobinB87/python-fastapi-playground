from enum import Enum

from pydantic import BaseModel, Field


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    count: int = Field(gt=0)
    id: int = Field(ge=0)
    category: Category


Selection = dict[str, str | int | float | Category | None]
