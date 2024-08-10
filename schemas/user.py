from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    google_id: str
    guardian_contact: str
    bulb_ip: str
    location_id: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    bulb_connection: bool
    pass

class UserResponse(UserBase):
    id: str
    pass

class UserInDB(UserBase):
    class Config:
        orm_mode = True
