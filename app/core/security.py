from datetime import datetime, timedelta, UTC
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITM, ACCESS_TOKEN_EXPIRE_MINUTES

class JWTService:
    
    def create_access_token(data:dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        print("JWT", jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITM))
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITM)
    
    
    def decode_token(token:str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITM])
            return payload
        except JWTError:
            return {}