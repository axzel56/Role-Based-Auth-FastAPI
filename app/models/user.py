from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False, deferred=True)
    role = relationship("Role", back_populates="users")
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    
    def __repr__(self):
        return f"<User(email= {self.email}, role= {self.role.name})>"