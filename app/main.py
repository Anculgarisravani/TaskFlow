from fastapi import FastAPI

from app.routers import projects, tasks, users

app = FastAPI(
    title="TaskFlow API",
    description="Enterprise Task & Workflow Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to TaskFlow API"}


app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(users.router)

from app import models
from app.database import engine, Base

Base.metadata.create_all(bind=engine)