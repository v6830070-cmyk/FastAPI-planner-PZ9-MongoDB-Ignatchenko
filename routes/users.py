from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])
user_database = Database(User)

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User exists")
    await user_database.save(user)
    # ПЕРСОНАЛИЗАЦИЯ
    return {"message": "Пользователь успешно зарегистрирован! (Выполнил: Игнатченко Владислав)"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user_exist.password == user.password:
        # ПЕРСОНАЛИЗАЦИЯ
        return {"message": "Пользователь успешно вошел! (Выполнил: Игнатченко Владислав)"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")