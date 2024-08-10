#### fastapi 기본포맷 ####

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert, select, update, delete
from models.test_item import TestItem
from datetime import datetime


class CRUDTestItem:
    @staticmethod
    def insert(db: Session, *, id: str, value: int):
        test_item = TestItem(id=id, value=value)
        try:
            db.add(test_item)
            db.commit()
            db.refresh(test_item)
        except IntegrityError:
            db.rollback()
            raise ValueError("Test item with ID already exists.")
        return test_item

    @staticmethod
    def get(db: Session, id: str):
        return db.get(TestItem, id)

    @staticmethod
    def get_all(db: Session):
        return db.scalars(
            select(TestItem)
        ).all()

    @staticmethod
    def update(db: Session, *, id: str, value: str):
        # Update the test_item
        updated_test_item = db.get(TestItem, id)
        if updated_test_item:
            updated_at = datetime.now()
            db.query(TestItem).filter(TestItem.id == id).update({"value": value, "updated_at": updated_at})
            db.commit()
            db.refresh(updated_test_item)

        return updated_test_item

    @staticmethod
    def delete(db: Session, id: str):
        deleted_test_item = db.get(TestItem, id)
        if deleted_test_item:
            db.delete(deleted_test_item)
            db.commit()
        return deleted_test_item


#### 싱글톤 객체 생성 ####
crud_test_item = CRUDTestItem()
