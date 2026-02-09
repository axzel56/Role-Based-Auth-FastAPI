from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import TokenResponse
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.utils.hashing import PasswordHasher
from app.core.security import JWTService

class AuthService:
    
    def __init__(self, db:Session):
        self.user_repo = UserRepository(db)
        self.hasher = PasswordHasher()
        
    
    def signup(self, data:UserCreate) -> User:
        existing_user = self.user_repo.get_by_email(data.email)
        if existing_user :
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        
        hashed_password = self.hasher.hash(data.password)
        
        user = User(
            email = data.email,
            password = data.password,
            hashed_password = hashed_password,
            role_id= data.role_id
        )
        
        return self.user_repo.create(user)
    
    def login(self, email: str, password: str) -> dict:
        user = self.user_repo.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        if not self.hasher.verify(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Credentials"
            )
        
        token_data = {
            "sub": user.email,
            "role": user.role.name,
        }
        
        access_token =  JWTService.create_access_token(token_data)
        return {
            "access_token" : access_token,
            "token_type" : "bearer",
            "message" :  "Welcome!" if user.role.name == "admin" else "Welcome Non Admin"
        }
        
        