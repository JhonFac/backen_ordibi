import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las partes de la URL de la base de datos desde las variables de entorno
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER", "mysql")  # Si el driver no está definido en el .env, asume 'mysql'

# Construir la URL de la base de datos
SQLALCHEMY_DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    # Intenta conectar a la base de datos
    engine.connect()
    print("Conexion a la base de datos exitosa")
except Exception as e:
    # Si hay un error al conectar, imprime un mensaje de error y finaliza la aplicación
    print(f"Error al conectar a la base de datos: {e}")
    exit()

# Si la conexión se establece correctamente, continúa con la declaración de la base de datos y la creación de la sesión
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()