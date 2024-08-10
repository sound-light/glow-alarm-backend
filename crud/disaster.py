from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.disaster import Disaster
from datetime import datetime
import uuid

class CRUDDisaster:
    @staticmethod
    def insert(db: Session, *, id: str, disaster_time: datetime, disaster_level: str, disaster_message: str, location_id: int):
        disaster = Disaster(id=id, disaster_time=disaster_time, disaster_level=disaster_level, disaster_message=disaster_message, location_id=location_id)
        try:
            db.add(disaster)
            db.commit()
            db.refresh(disaster)
        except IntegrityError:
            db.rollback()
            raise ValueError("Disaster with ID already exists.")
        return disaster

    @staticmethod
    def get(db: Session, id: str):
        return db.get(Disaster, id)

    @staticmethod
    def get_all(db: Session):
        return db.query(Disaster).all()
    
    @staticmethod
    def get_all_by_location_id(db: Session, location_id: str):
        return db.query(Disaster).filter(Disaster.location_id == location_id).all()

    @staticmethod
    def update(db: Session, *, id: str, disaster_time: datetime, disaster_level: str, disaster_message: str, location_id: int):
        updated_disaster = db.get(Disaster, id)
        if updated_disaster:
            updated_at = datetime.now()
            db.query(Disaster).filter(Disaster.id == id).update({"disaster_time": disaster_time, "disaster_level": disaster_level, "disaster_message": disaster_message, "location_id": location_id, "updated_at": updated_at})
            db.commit()
            db.refresh(updated_disaster)

        return updated_disaster

    @staticmethod
    def delete(db: Session, id: str):
        deleted_disaster = db.get(Disaster, id)
        if deleted_disaster:
            db.delete(deleted_disaster)
            db.commit()
        return deleted_disaster


# 싱글톤 객체 생성
crud_disaster = CRUDDisaster()