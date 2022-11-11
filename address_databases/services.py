from fastapi import HTTPException, status
from typing import List
from . import models
from datetime import datetime


'''performing all database queries'''


async def create_new_address(request, database) -> models.Address:
    new_address = models.Address( address=request.address,
                                modified_at=datetime.now(),coordinate=request.cordinate)              
    print(f"New Address -->{new_address}")
    database.add(new_address)
    database.commit()
    database.refresh(new_address)
    return new_address
    #i have checked to validate cordinates by google apis howere due to lack of credit card i don't have access to google apis free trial

async def get_address_listing(database) -> List[models.Address]:
    addresses = database.query(models.Address).all()
    return addresses


async def get_address_by_id(address_id,database):
    address = database.query(models.Address).filter_by(
        id=address_id).first()
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address Not Found !"
        )
    return address


async def delete_address_by_id(address_id,database):
    database.query(models.Address).filter(
        models.Address.id == address_id).delete()
    database.commit()


async def update_address_by_id(request, address_id, database):
    address = database.query(models.Address).filter_by(
        id=address_id).first()
    print("Adress -->",address)
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address Not Found !"
        )
    address.address = request.address if request.address else address.address
    database.commit()
    database.refresh(address)
    return address
