from typing import Optional, List
from pydantic import BaseModel


class AddressBase(BaseModel):
    id: Optional[int]
    modified_at: Optional[str]
    address_coordinate:str
    address: str


    class Config:
        orm_mode = True


class AddressUpdate(BaseModel):
    address: Optional[str]
    address_coordinate:Optional[str]
    

    class Config:
        orm_mode = True


class MultipleAddress(BaseModel):

    data: List[AddressBase]


class AddressList(BaseModel):
    id: Optional[int]
    modified_at: Optional[str]
    address_coordinate:str
    address: str

    class Config:
        orm_mode = True
