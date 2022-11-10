#fastapi
from fastapi import FastAPI
app = FastAPI()

#basic imports
import constants
from address_databases import schemas,services,models
from address_databases import database as db

#fastapi imports
from typing import List
from fastapi import status,Depends
from sqlalchemy.orm import Session 


# @app.get(constants.root)
# async def root():
#     return {"message": "Hello, I am Om Prakash"}
models.Base.metadata.create_all(bind=db.engine)

@app.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.AddressBase)
async def create_new_address(request: schemas.AddressBase, database: Session = Depends(db.get_db)):
        print(request)
        response= await services.create_new_address(request=request,database=database)
        print("--->",response)
        return response

@app.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.AddressList])
async def get_all_address(datbase: Session = Depends(db.get_db)):
    response= await services.get_address_listing(database=datbase)
    return response

@app.get('/addressbyid/{address_id}',status_code=status.HTTP_200_OK,response_model=schemas.AddressBase)
async def get_address_by_id(address_id:int,database: Session = Depends(db.get_db)):
        return await services.get_address_by_id(address_id=address_id,database=database)

@app.delete("/deleteaddressid/{address_id}",status_code=status.HTTP_200_OK)
async def delete_address_by_id(address_id: int, database: Session=Depends(db.get_db)):
        return await services.delete_address_by_id(address_id=address_id,database=database)


@app.put("/updateaddressbyid/{address_id}",status_code=status.HTTP_200_OK,response_model=schemas.AddressBase)
async def update_address_by_id(request:schemas.AddressBase, address_id: int,databse: Session=Depends(db.get_db)):
        print("reuest-->",request)
        return await services.update_address_by_id(request=request,address_id=address_id,database=databse)