from api.database import db_operations as db
from api.schemas.category import CategoryResponse
from core.models import Category
from fastapi import HTTPException


def create(data, model, response):

    try:
        if model.__tablename__ == "locations":
            get_by_id(data.category_id, Category, CategoryResponse)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Category no fund: {str(e)}")

    try:
        respose_db =  db.create(model(**data.dict()))
        return response(**respose_db.__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving to database: {str(e)}")


def get_all(model, response):
    try:
        respose_dbs =  db.get_all(model)
        return [response(**respose_db.__dict__) for respose_db in respose_dbs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying the database: {str(e)}")


def get_all_order(model, response):

    try:
        respose_dbs =  db.get_all_order(model)
        return [response(**respose_db.__dict__) for respose_db in respose_dbs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying the database: {str(e)}")


def get_by_id_relation(id, model, response):

    try:
        respose_db =  db.get_by_id_relation(id, model)
        return response(**respose_db.__dict__)
    except Exception:
        raise HTTPException(status_code=404, detail="Object not found")

def get_by_id(id, model, response):

    try:
        respose_db =  db.get_by_id(id, model)
        return response(**respose_db.__dict__)
    except Exception:
        raise HTTPException(status_code=404, detail="Object not found")



def update(id, update_data, model, response):

    respose_db = db.get_by_id(id, model)
    if respose_db is None:
        raise HTTPException(status_code=404, detail="Object not found")
    try:
        respose_db = db.update(id, model, update_data)
        return {"message": "Object updated successfully", "data": respose_db}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating location: {str(e)}")


def dalete(id, model):
    respose_db = db.get_by_id(id, model)
    if respose_db is None:
        raise HTTPException(status_code=404, detail="Object not found")

    try:
        db.delete(respose_db)
        return {"message": "Successfully removed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting data: {str(e)}")




