from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User, UserRole, UserStatus


def get_current_user(db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.role == UserRole.admin).first()
    print("ROLE:", user.role)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if user.status != UserStatus.active:
        raise HTTPException(status_code=403, detail="Inactive user")

    return user


def role_required(allowed_roles: list):
    def wrapper(user: User = Depends(get_current_user)):
        if user.role.value not in [role.value if hasattr(role, "value") else role for role in allowed_roles]:
            raise HTTPException(status_code=403, detail="Access denied")
        return user

    return wrapper