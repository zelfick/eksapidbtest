# Create a model to interact with the postgress database 
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base
#from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

# define the class db which inherits from Base
class Userdb(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_done = Column(Boolean, default=False)
    

# create the previous database defined
Base.metadata.create_all(engine)