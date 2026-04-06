from fastapi import FastAPI
from app.database import Base, engine

# Import models
from app.models import user, record

# Import routes

from app.routes import user_routes, record_routes
from app.routes import dashboard_routes
# 👇 CREATE APP FIRST
app = FastAPI()

# 👇 THEN include router
app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)
# Create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Finance Backend Running"}

   

