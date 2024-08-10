import enum
import uuid

from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
class LightColor(str, enum.Enum):
    RED = "Red"
    BLUE = "Blue"
    ORANGE = "Orange"
    PURPLE = "Purple"
    WHITE = "White"
    YELLOW = "Yellow"
    GREEN = "Green"

class Alarm(Base, TimeStampedModel):
    __tablename__ = "alarm"

    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    alarm_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    name = Column(String(255), nullable=True, default="Default Alarm")
    repeat_day = Column(String(7))
    light_color= Column(Enum(LightColor),  default = LightColor.GREEN)
    alarm_status = Column(Boolean,  default=False)
    user_id = Column(String(255), ForeignKey('user.id'))
    user = relationship("User", back_populates="alarms")