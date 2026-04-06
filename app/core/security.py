from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User


# Mock authentication (replace with JWT in real system)
def get_current_user(db: Session = Depends(get_db)) -> User:
    """
    Simulates fetching the currently logged-in user.
    In a real system, this would decode a JWT token
    and fetch the user from the database.
    """

    # For demo: fetch first active admin user
    user = db.query(User).filter(User.role == "admin").first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if user.status != "active":
        raise HTTPException(status_code=403, detail="Inactive user")

    return user


def role_required(allowed_roles: list):
    """
    Dependency to restrict access based on user roles.
    Usage: Depends(role_required(["admin", "analyst"]))
    """

    def wrapper(user: User = Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return user

    return wrapper