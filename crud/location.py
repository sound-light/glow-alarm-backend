from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete
from models.location import Location
import uuid

class CRUDLocation:
    @staticmethod
    def insert(db: Session, *, location_code: str, location_name: str):
        location = Location(location_code=location_code, location_name=location_name)
        try:
            db.add(location)
            db.commit()
            db.refresh(location)
        except IntegrityError:
            db.rollback()
            raise ValueError("Location with ID already exists.")
        return location

    @staticmethod
    def get(db: Session, id: str):
        return db.get(Location, id)

    @staticmethod
    def get_all(db: Session):
        return db.query(Location).all()

    @staticmethod
    def update(db: Session, *, id: str, location_code: int, location_name: str):
        updated_location = db.get(Location, id)
        if updated_location:
            db.query(Location).filter(Location.id == id).update({"location_code": location_code, "location_name": location_name})
            db.commit()
            db.refresh(updated_location)

        return updated_location

    @staticmethod
    def delete(db: Session, id: str):
        deleted_location = db.get(Location, id)
        if deleted_location:
            db.delete(deleted_location)
            db.commit()
        return deleted_location


# 싱글톤 객체 생성
crud_location = CRUDLocation()