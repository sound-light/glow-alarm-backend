from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LocationBase(BaseModel):
    
    location_code: str
    location_name: str


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: str
    pass

class LocationInDB(LocationBase):
    class Config:
        orm_mode = True

