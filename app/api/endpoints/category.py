from api.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from api.services import services
from core.models import Category
from fastapi import APIRouter

category_router = APIRouter()

@category_router.post("/")
def create(category: CategoryCreate):
    return services.create(category, Category, CategoryResponse)



@category_router.get("/")
def get_all():
    return services.get_all(Category, CategoryResponse)


@category_router.get("/{id}")
def get_by_id(id: int):
    return services.get_by_id(id, Category, CategoryResponse)



@category_router.patch("/{id}")
def update(id: int , category: CategoryUpdate):
    return services.update(id, category, Category, CategoryResponse)



@category_router.delete("/{id}")
def delete(id: int):

    return services.dalete(id, Category)
