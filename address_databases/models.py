from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)     #id is primary key
    modified_at = Column(DateTime)                                             #to track latest address
    address = Column(String)                                                   #address data
    address_cordinate = Column(String)                                         #address cordinates