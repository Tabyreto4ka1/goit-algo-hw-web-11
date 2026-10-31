from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ContactUpdate, ContactResponse, ContactSearch
from src.repository import contacts as repository_contacts


router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def reads_contacts(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return await repository_contacts.get_contacts(skip,limit,db)

@router.get("/search", response_model=List[ContactResponse])
async def search_contacts(body:ContactSearch=Depends(),db:Session=Depends(get_db)):
    return await repository_contacts.search_contact(body,db)

@router.get("/birthdays", response_model=List[ContactResponse])
async def upcoming_birthdays(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return await repository_contacts.birthday_contacts(skip,limit,db)

@router.get("/{id}", response_model=ContactResponse)
async def reads_contacts(id:int,db:Session=Depends(get_db)):
    return await repository_contacts.get_contact(id,db)

@router.post("/", response_model=ContactResponse)
async def create_contact(body:ContactModel,db:Session=Depends(get_db)):
    return await repository_contacts.create_contact(body, db)

@router.put("/{id}", response_model=ContactResponse)
async def update_contact(id:int, body:ContactUpdate, db:Session=Depends(get_db)):
    update_contact=await repository_contacts.update_contact(id,body,db)
    if update_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return update_contact


@router.delete("/{id}",response_model=ContactResponse)
async def remove_contact(id:int, db:Session=Depends(get_db)):
    del_contact=await repository_contacts.remove_contact(id,db)
    if del_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return del_contact

