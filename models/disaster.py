from db.base import Base
from models.columns.timestamp import TimeStampedModel
from datetime import datetime
from sqlalchemy import Column, String, DateTime ,ForeignKey, Integer
from sqlalchemy.orm import relationship
import uuid

class Disaster(Base, TimeStampedModel):
    __tablename__ = "disaster"
    
    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    disaster_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    disaster_level = Column(String(20), nullable=False)
    disaster_message = Column(String(20), nullable=False)

    location_id = Column(String(255), ForeignKey('location.id'))
    location = relationship("Location", back_populates="disasters")