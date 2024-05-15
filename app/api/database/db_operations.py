from api.schemas.locations import LocationResponseRelations
from core.database import SessionLocal
from sqlalchemy import asc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload


# Función para obtener una nueva sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create(db_location):
    with SessionLocal() as db:
        try:
            db.add(db_location)
            db.commit()
            db.refresh(db_location)
            return db_location
        except SQLAlchemyError as e:
            db.rollback()
            raise e
        

def get_all(model):
    with SessionLocal() as db:
        try:
            if model.__tablename__ == "locations":
                locations = db.query(model).options(joinedload(model.category)).all()
                return [LocationResponseRelations.from_orm(location) for location in locations]
            print('sigio')
            return db.query(model).all()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

def get_all_order(model):
    with SessionLocal() as db:
        try:
            return db.query(model).options(joinedload(model.category)).order_by(asc(model.nreviewedame)).all()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

def get_by_id_relation(id, model):
    with SessionLocal() as db:
        try:
            location = db.query(model).options(joinedload(model.category)).filter(model.id == id).first()
            return LocationResponseRelations.from_orm(location)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

def get_by_id(id, model):
    with SessionLocal() as db:
        try:
            return db.query(model).get(id)
        except SQLAlchemyError as e:
            db.rollback()
            raise e


def update(id, model, update_data):
    with SessionLocal() as db:
        try:
            response_db = db.query(model).get(id)
            for key, value in update_data.dict(exclude_unset=True).items():
                setattr(response_db, key, value)
            db.commit()
            db.refresh(response_db)
            return response_db

        except SQLAlchemyError as e:
            db.rollback()
            raise e

def delete(object):
    with SessionLocal() as db:
        try:
            db.delete(object)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise e
