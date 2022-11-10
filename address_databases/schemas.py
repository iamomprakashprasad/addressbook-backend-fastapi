from typing import Optional, List
from pydantic import BaseModel, constr


class AddressBase(BaseModel):
    id: Optional[int]
    created_date: Optional[str]
    address: str
    class Config:
        orm_mode = True


class AddressUpdate(BaseModel):
    address: Optional[str]

    class Config:
        orm_mode = True

class MultipleAddress(BaseModel):

    data: List[AddressBase]

class AddressList(BaseModel):
    address: Optional[str]

    class Config:
        orm_mode = True