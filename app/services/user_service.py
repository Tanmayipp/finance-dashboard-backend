from sqlalchemy.orm import Session
from app.models.user import User


def create_user(db: Session, user_data):
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password,  # ideally hashed
        role=user_data.role,
        status="active"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, update_data):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


def deactivate_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    user.status = "inactive"
    db.commit()
    db.refresh(user)

    return user