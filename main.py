# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# FastAPIアプリの初期化
app = FastAPI()

# データモデルの定義
class User(BaseModel):
    name: str
    email: str

# エンドポイントの定義
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} with email {user.email} has been created"}