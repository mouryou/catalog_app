import os
import sys
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Catagory(Base):
    __tablename__ = 'catagory'

    name = Column(String(50), nullable=False, primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    name = Column(String(50), nullable=False, primary_key=True)
    description = Column(String(500))
    catagory_name = Column(String, ForeignKey('catagory.name'))
    catagory = relationship(Catagory)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'catagory_name': self.catagory_name,
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)