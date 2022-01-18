from ast import Str
from xmlrpc.client import Boolean
from sqlalchemy import Table, Column, Integer, MetaData, String, TIMESTAMP, Float, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

# metadata_obj = MetaData()

# keystrokes = Table('keystrokes', metadata_obj,
#             Column('id', Integer, primary_key=True),
#             Column('key', String, nullable=False),
#             Column('press_timestamp', Float, nullable=False),
#             Column('release_timestamp', Float, nullable=False))

# users = Table('users', metadata_obj,
#             Column('id', Integer, primary_key=True),
#             Column('name', String, nullable=False),
#             Column('email', String, nullable=False),
#             Column('phoneNumber', String, nullable=False),
#             Column('country', String, nullable=True),
#             Column('city', String, nullable=True),
#             Column('password', String, nullable=False),
#             Column('gender', String, nullable=True))

Base = declarative_base()




class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phonenumber = Column(String, unique=True)
    country = Column(String)
    city = Column(String)
    password = Column(String, nullable=False)
    gender = Column(String)
    enable_2fa = Column(Boolean, default=False)
    otp_secret = Column(String, nullable=True)


class Keystroke(Base):
    __tablename__ = 'keystroke'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    key = Column(String)
    pressed_timestamp = Column(TIMESTAMP)
    released_timestamp = Column(TIMESTAMP)