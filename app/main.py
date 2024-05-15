import uvicorn
from core.application import create_api
from core.database import engine

api = create_api()


# Conectar a la base de datos al iniciar la aplicación
@api.on_event("startup")
async def startup_event():
    engine.connect()

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)