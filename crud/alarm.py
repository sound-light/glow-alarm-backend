from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.alarm import Alarm
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from pytz import utc
import uuid
import time
import random

scheduler = BackgroundScheduler(timezone=utc)

class CRUDAlarm:
    @staticmethod
    def insert(db: Session, *, alarm_time: datetime, name: str, repeat_day: str, light_color: str, alarm_status: bool, user_id: str):
        try:
            alarm = Alarm(alarm_time=alarm_time, name=name, repeat_day=repeat_day, light_color=light_color, alarm_status=alarm_status, user_id=user_id)
            db.add(alarm)
            db.commit()
            db.refresh(alarm)
            return alarm
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Alarm creation failed: {str(e)}")

    @staticmethod
    def get(db: Session, id: str):
        return db.get(Alarm, id)

    @staticmethod
    def get_all(db: Session):
        return db.query(Alarm).all()
    
    @staticmethod
    def get_all_by_user_id(db: Session, user_id: str):
        return db.query(Alarm).filter(Alarm.user_id == user_id).all()

    @staticmethod
    def update(db: Session, *, id: str, alarm_time: datetime, repeat_day: str, light_color: str, alarm_status: bool, user_id: str):
        updated_alarm = db.get(Alarm, id)
        if updated_alarm:
            updated_at = datetime.now()
            db.query(Alarm).filter(Alarm.id == id).update({"alarm_time": alarm_time, "repeat_day": repeat_day, "light_color": light_color, "alarm_status": alarm_status, "user_id": user_id, "updated_at": updated_at})
            db.commit()
            db.refresh(updated_alarm)

        return updated_alarm

    @staticmethod
    def delete(db: Session, id: str):
        deleted_alarm = db.get(Alarm, id)
        if deleted_alarm:
            db.delete(deleted_alarm)
            db.commit()
        return deleted_alarm

    @staticmethod
    def turn_off_alarm(db: Session, id: str):
        alarm = db.get(Alarm, id)
        if alarm:
            alarm.alarm_status = False
            alarm.updated_at = datetime.now()
            db.commit()
            db.refresh(alarm)
            return alarm
        return None



# 싱글톤 객체 생성
crud_alarm = CRUDAlarm()
