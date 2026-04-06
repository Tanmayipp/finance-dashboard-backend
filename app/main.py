from fastapi import FastAPI
from app.database import Base, engine

# Import models
from app.models import user, record

# Import routes
from app.routes import user_routes, record_routes, dashboard_routes

from app.database import SessionLocal
from app.models.user import User, UserRole, UserStatus

app = FastAPI()

# ✅ STEP 1: Create tables FIRST
Base.metadata.create_all(bind=engine)


# ✅ STEP 2: Then create default user
def create_default_admin():
    db = SessionLocal()
    try:
        existing_user = db.query(User).first()

        if not existing_user:
            admin = User(
                name="Admin",
                email="admin@test.com",
                password="123",
                role=UserRole.admin,
                status=UserStatus.active
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()


create_default_admin()


# ✅ STEP 3: Then include routes
app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)


@app.get("/")
def root():
    return {"message": "Finance Backend Running"}