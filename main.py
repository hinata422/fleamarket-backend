from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPIアプリの初期化
app = FastAPI()

# 仮のデータベース（メモリ上）
users = []

# データモデルの定義
class User(BaseModel):
    name: str
    email: str
    password: str

# ルートエンドポイント
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# 新規ユーザー登録
@app.post("/users/")
def create_user(user: User):
    # 既に登録されているか確認
    if any(u['email'] == user.email for u in users):
        raise HTTPException(status_code=409, detail="User already exists")

    # IDを自動で付与
    user_id = len(users) + 1

    # 仮のデータベースに追加
    users.append({
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "password": user.password  # 実際はハッシュ化が望ましい
    })

    return {"message": f"User {user.name} with email {user.email} has been created"}

# 全ユーザーの取得
@app.get("/users/")
def get_users():
    return {"users": users}

# 特定のユーザーの取得
@app.get("/users/{user_id}")
def get_user(user_id: int):
    # メモリ上のデータから該当するIDを検索
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
