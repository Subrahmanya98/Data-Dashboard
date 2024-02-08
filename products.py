
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(description="Product name", example="v")
    description:str = Field(description="Product description", default=None)
    