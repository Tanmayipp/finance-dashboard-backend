from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.record import Record


def create_record(db: Session, user, record_data):
    record = Record(
        user_id=user.id,
        amount=record_data.amount,
        type=record_data.type,
        category=record_data.category,
        date=record_data.date,
        notes=record_data.notes
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_records(
    db: Session,
    user,
    type: str = None,
    category: str = None,
    start_date = None,
    end_date = None
):
    query = db.query(Record).filter(Record.user_id == user.id)

    if type:
        query = query.filter(Record.type == type)

    if category:
        query = query.filter(Record.category == category)

    if start_date:
        query = query.filter(Record.date >= start_date)

    if end_date:
        query = query.filter(Record.date <= end_date)

    return query.all()


def update_record(db: Session, user, record_id: int, update_data):
    record = db.query(Record).filter(
        Record.id == record_id,
        Record.user_id == user.id
    ).first()

    if not record:
        return None

    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)

    return record


def delete_record(db: Session, user, record_id: int):
    record = db.query(Record).filter(
        Record.id == record_id,
        Record.user_id == user.id
    ).first()

    if not record:
        return False

    db.delete(record)
    db.commit()

    return True