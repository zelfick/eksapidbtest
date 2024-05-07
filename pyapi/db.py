# Define connection and parameters to interact with the postgresdb
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from config import settings

#database_url = 'postgresql://postgres:passwd@host.docker.internal/postgres' test docker database
#database_url = 'postgresql://username:password@host/database_name'

database_url = settings.POSTGRES_URL
print("Database URL is ",database_url)

# A database engine to interact with the database
engine = create_engine(database_url)


# We create now a session to the database
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# instance of the session defined
opensession = Session()