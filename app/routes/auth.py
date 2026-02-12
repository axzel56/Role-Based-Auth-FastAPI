from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/token",
    response_model=TokenResponse
)
def login_oauth2(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    service = AuthService(db)
    return service.login(form_data.username, form_data.password)
    

@router.post(
    "/signup",
    response_model= UserRead,
    status_code=status.HTTP_201_CREATED
)
def signup(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    service = AuthService(db)
    return service.signup(data)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    response = service.login(data.email, data.password)
    print(response)
    return response
