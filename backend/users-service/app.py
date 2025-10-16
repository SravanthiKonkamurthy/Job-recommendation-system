from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users = []

@app.post("/signup")
def signup(user: User):
    users.append(user.dict())
    return {"message": "User registered successfully"}

@app.get("/users")
def get_users():
    return users
