#!/usr/bin/env python3
''' User model module.
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    ''' SQLAlchemy model(User) for a db table(users)
    with the following attributes:
        - id: int primary key
        - email: non-nullable string
        - hashed_password: non-nullable string
        - session_id: nullable string
        - reset_token: nullable string
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        return f'User: id={self.id}'
