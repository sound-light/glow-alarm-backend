#### fastapi 기본포맷 ####

from pydantic import BaseModel


class TestItemBase(BaseModel):
    id: str
    value: int


class TestItemCreate(TestItemBase):
    pass


class TestItemUpdate(TestItemBase):
    pass


class TestItemInDB(TestItemBase):
    class Config:
        orm_mode = True
