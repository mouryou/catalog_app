import os
import sys
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False, primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500))
    category_name = Column(String, ForeignKey('category.name'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_name': self.category_name,
        }


engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == '__main__':
    # Add categories to the database
    try:
        for categoryName in ['Soccer', 'Basketball', 'Baseball', 'Frisbee',
                             'Snowboarding', 'Rock Climbing', 'Football',
                             'Skating', 'Hockey']:
            newCategory = Category(name=categoryName)
            session.add(newCategory)
            session.commit()
        print("Added categories successfully")
    except:
        print("Categories have already been added")
