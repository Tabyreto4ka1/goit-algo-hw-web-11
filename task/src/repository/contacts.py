from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Session
import datetime
from src.database.models import Contact
from src.schemas import ContactModel, ContactResponse,ContactUpdate, ContactSearch

async def get_contacts(skip:int, limit:int, db:Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

async def get_contact(id: int,db:Session) -> Contact:
    return db.query(Contact).filter(Contact.id==id).first()

async def create_contact(body:ContactModel, db:Session) -> Contact:
    contact=Contact(name=body.name, 
                    last_name=body.last_name, 
                    email=body.email,
                    phone_number=body.phone_number, 
                    birthday=body.birthday, 
                    additional=body.additional
                    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(id:int, body: ContactUpdate, db:Session)->Contact | None :
    contact=db.query(Contact).filter(Contact.id==id).first()
    if contact:
        contact.name=body.name
        contact.last_name=body.last_name
        contact.email=body.email
        contact.phone_number=body.phone_number
        contact.birthday=body.birthday
        contact.additional=body.additional
        db.commit()
    return contact

async def remove_contact(id:int, db:Session) -> Contact | None:
    contact=db.query(Contact).filter(Contact.id==id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

async def birthday_contacts(skip:int, limit:int, db:Session)->List[Contact]:
    contacts=[]
    today = datetime.datetime.now(datetime.timezone.utc).date()
    for i in range(0,8):
        date=today+datetime.timedelta(days=i)
        date_str = date.strftime("%m-%d")
        contacts.extend(db.query(Contact).filter(func.to_char(Contact.birthday, "MM-DD")==date_str).offset(skip).limit(limit).all())
    return contacts
        
async def search_contact(body: ContactSearch,db:Session)-> List[Contact]:
    query = db.query(Contact)
    if body.name:
        query=query.filter(Contact.name==body.name)
    if body.last_name:
        query=query.filter(Contact.last_name==body.last_name)
    if body.email:
        query=query.filter(Contact.email==body.email)
    return query.all()