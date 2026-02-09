from fastapi import APIRouter, Depends
from app.dependencies.auth import RoleChecker
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role

router = APIRouter(prefix="/users", tags=["Users"])

admin_only = RoleChecker(["admin"])
user_or_admin = RoleChecker(["users", "admin"])

def get_admin_user(db : Session = Depends(get_db)):
    return db.query(User).join(Role).filter(Role.name == "admin").all()


def get_non_admin(db: Session = Depends(get_db)):
    return db.query(User).join(Role).filter(Role.name == "users").all()

@router.get("/admin")
def admin_dashboard(user= Depends(admin_only), admins=Depends(get_admin_user), non_admins= Depends(get_non_admin)):
    # print(get_admin_user())
    return {
        
        "admins" : [u.email for u in admins],
        "non-admins" : [u.email for u in non_admins],
        "message": f"Welcome admin {user.email}"
    }
    
    
@router.get("/me")
def read_me(user=Depends(user_or_admin)):
    return {
        "id" : user.id,
        "email" : user.email,
        "role" : user.role.name
    }