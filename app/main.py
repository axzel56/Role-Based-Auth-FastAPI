from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user, role
from app.routes import auth, users

app = FastAPI(title="RBAC FastAPI")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def health_check():
    return {"status": "ok"}
