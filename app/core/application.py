from logging import shutdown

from api.endpoints.category import category_router
from api.endpoints.locations import location_router
from core.database import Base, engine
from fastapi import FastAPI


def create_api():
    api = FastAPI()
    api.include_router(location_router, prefix="/locations", tags=["locations"])
    api.include_router(category_router, prefix="/categories", tags=["categories"])
    
    # Función para crear las tablas en la base de datos si no existen
    def create_tables():
        Base.metadata.create_all(bind=engine)

    # Agregar la función create_tables al evento de inicio de la aplicación
    @api.on_event("startup")
    async def startup_event():
        create_tables()


    return api
