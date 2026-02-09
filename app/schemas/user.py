from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: EmailStr
    
# For input only
class UserCreate(UserBase):
    password: str
    role_id: int

# For Role Output only    
class RoleRead(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes= True)

# For User Output only
class UserRead(UserBase):
    id: int
    role: RoleRead
    
    model_config = ConfigDict(from_attributes=True)