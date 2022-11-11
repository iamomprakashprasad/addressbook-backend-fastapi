# fastapi
from address_databases import schemas, services, models
from sqlalchemy.orm import Session
from fastapi import status, Depends
from typing import List
from address_databases import database as db
import constants
from fastapi import FastAPI
app = FastAPI()

# basic imports

# fastapi imports

# created databases tables
models.Base.metadata.create_all(bind=db.engine)

# create an address
@app.post(constants.root, status_code=status.HTTP_201_CREATED, response_model=schemas.AddressBase)
async def create_new_address(request: schemas.AddressBase, database: Session = Depends(db.get_db)):
        response = await services.create_new_address(request=request, database=database)
        return response

# get all address
@app.get(constants.root, status_code=status.HTTP_200_OK, response_model=List[schemas.AddressList])
async def get_all_address(datbase: Session = Depends(db.get_db)):
    response = await services.get_address_listing(database=datbase)
    return response

# get specific address by address id
@app.get(constants.get_address_by_id, status_code=status.HTTP_200_OK, response_model=schemas.AddressBase)
async def get_address_by_id(address_id: int, database: Session = Depends(db.get_db)):
    return await services.get_address_by_id(address_id=address_id, database=database)

# delete specific address by address id
@app.delete(constants.delete_address_by_id, status_code=status.HTTP_200_OK)
async def delete_address_by_id(address_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_address_by_id(address_id=address_id, database=database)

# update specific address by address id
@app.put(constants.update_address_by_id, status_code=status.HTTP_200_OK, response_model=schemas.AddressBase)
async def update_address_by_id(request: schemas.AddressBase, address_id: int, databse: Session = Depends(db.get_db)):
    return await services.update_address_by_id(request=request, address_id=address_id, database=databse)

# get addresses by coordinates
@app.get(constants.get_address_by_coordinate, status_code=status.HTTP_200_OK, response_model=List[schemas.AddressList])
async def get_address_by_coordinates(address_coordinate: str, database: Session = Depends(db.get_db)):
    return await services.get_address_by_coordinates(address_coordinate=address_coordinate, database=database)