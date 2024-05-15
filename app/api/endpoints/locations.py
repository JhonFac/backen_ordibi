from api.schemas.locations import (
    LocationCreate,
    LocationResponse,
    LocationResponseRelations,
    LocationUpdate,
)
from api.services import services
from core.models import Location
from fastapi import APIRouter

location_router = APIRouter()

@location_router.post("/")
def create_location(location: LocationCreate):
    return services.create(location, Location, LocationResponse)


@location_router.get("/")
def get_all():
    return services.get_all(Location, LocationResponseRelations)


@location_router.get("/order")
def get_by_id():
    return services.get_all_order(Location, LocationResponseRelations)


@location_router.get("/{id}")
def get_by_id_relation(id: int):
    return services.get_by_id_relation(id, Location, LocationResponseRelations)



@location_router.patch("/{id}")
def update_location(id: int , location: LocationUpdate):
    return services.update(id, location, Location, LocationResponse)



@location_router.delete("/{id}")
def delete(id: int):

    return services.dalete(id, Location)
