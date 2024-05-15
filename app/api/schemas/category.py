from typing import Optional

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Habilita el uso de from_orm
