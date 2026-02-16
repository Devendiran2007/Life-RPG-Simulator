from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from .. models import User
from .. schemas import UserCreate , UserResponse , UserLogin
from .. database import get_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

def hash_password(password: str):
    return pwd_context.hash(password)

def check_password(password: str , hashed_password: str):
    return pwd_context.verify(password, hashed_password)    

@router.post("/register" , response_model = UserResponse)
def register(user : UserCreate , db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code = 400 , detail = "Username Already Exists")
    new_user = User(
        username = user.username,
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login" , response_model = UserLogin)
def login(user: UserLogin , db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User,username == user.username).first()
    if not db_user:
        raise HTTPException(status_code= 400 , detail = "Invalid Username or PassWord")
    return UserResponse(db_user)


@router.put("/update" , response_model = UserCreate)
def update_user(user : UserCreate , db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code = 400 , detail = "User Not Found")
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = hash_password(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/delete" , response_model = UserResponse)
def delete_user(user : UserCreate , db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code = 400 , detail = "User Not Found")
    db.delete(db_user)
    db.commit()
    return db_user  


    

