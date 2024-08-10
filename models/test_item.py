#### fastapi 기본포맷 ####

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from db.base import Base
from models.columns.timestamp import TimeStampedModel


class TestItem(Base, TimeStampedModel):
    __tablename__ = "test_item"

    id = Column(String(20), primary_key=True, index=True)
    value = Column(Integer)