from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    name: str=Field(max_length=20)
    last_name: str=Field(max_length=20)
    email: str= Field(max_length=30)
    phone_number: str=Field(max_length=15)
    birthday: datetime
    additional: Optional[str] = Field(default=None, max_length=500)

class ContactResponse(ContactModel):
    id: int
    class Config:
        orm_mode = True

class ContactSearch(BaseModel):
    name: Optional[str]=Field(default=None,max_length=20)
    last_name: Optional[str]=Field(default=None,max_length=20)
    email: Optional[str]= Field(default=None,max_length=30)

class ContactUpdate(ContactModel):
    pass
