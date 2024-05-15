from typing import Optional

from pydantic import BaseModel

from .category import CategoryResponse


class LocationCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    nreviewedame: int
    category_id: int


class LocationUpdate(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    nreviewedame: Optional[int] = None
    category_id: Optional[int] = None


class LocationResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    nreviewedame: int
    category_id: int

class LocationResponseRelations(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    nreviewedame: int
    category: Optional[CategoryResponse]  # Relación anidada

    class Config:
        from_attributes = True  # Habilita el uso de from_orm