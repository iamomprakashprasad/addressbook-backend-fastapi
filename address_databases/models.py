from datetime import datetime
from sqlalchemy import Column, Float, ForeignKey, Text, DateTime, Integer, String



from .database import Base


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_date = Column(String)
    address = Column(String)


    # address_cordinate = Column(Text)