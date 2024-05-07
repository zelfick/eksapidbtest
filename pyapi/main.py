from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from userdb import Userdb
from db import opensession

# we instanciate the imported class FastAPI
app = FastAPI()

# we define the entry points for the API
@app.get("/")
async def root():
    return {"message": "Simple CRUD Database with FastAPI and Postgresql"}

# we define a post method to add to the database
@app.post("/api/v1/users/add")
async def add_user(id: int, name: str, is_done: bool = False):
    useradd = Userdb(id=id, name=name, is_done=is_done)
    opensession.add(useradd)
    opensession.commit()
    return {"Userdb added": useradd.name}

# we define a get operation for all users
@app.get("/api/v1/users")
async def get_all_users():
    userdb_query = opensession.query(Userdb)
    return userdb_query.all()

# we define a get operation to get userdata
@app.get("/api/v1/users/{id}")
async def get_user(id: int):
    user_query = opensession.query(Userdb).filter(Userdb.id == id)
    userdata = user_query.first()
    if userdata is None:
        raise HTTPException(status_code=404, details="userdata not found")
    return userdata

# we define a put operation to update records
@app.put("/api/v1/users/update/{id}")
async def update_user(
    id: int,
    new_name: str = "",
    is_complete: bool = False
):
    user_query = opensession.query(Userdb).filter(Userdb.id==id)
    user = user_query.first()
    if new_name:
        user.name = new_name
    user.is_done = is_complete
    opensession.add(user)
    opensession.commit()
    return {"user name updated for user id": user.id}

# we define a delete operation
@app.delete("/api/v1/users/delete/{id}")
async def delete_user(id: int):
    user = opensession.query(Userdb).filter(Userdb.id==id).first() # Userdb object
    opensession.delete(user)
    opensession.commit()
    return {"user deleted": user.name}