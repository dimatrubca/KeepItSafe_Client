from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from sqlalchemy.sql.schema import MetaData
from database.models import Base

engine = create_engine(
    'sqlite:///keepitsafe5.db', 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)
session = Session(bind=engine)

#metadata_obj.create_all(engine)
Base.metadata.create_all(engine)