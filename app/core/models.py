from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship

from .database import Base


# Define tus modelos aquí
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Especifica la longitud de VARCHAR
    latitude = Column(Float)
    longitude = Column(Float)
    nreviewedame = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Define la relación con la tabla de categorías
    category = relationship("Category", back_populates="locations")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)  # Especifica la longitud de VARCHAR

    # Definir la relación uno a muchos con Location
    locations = relationship("Location", back_populates="category")