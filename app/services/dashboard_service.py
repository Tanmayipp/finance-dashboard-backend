from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.record import Record


def get_summary(db: Session, user):
    total_income = db.query(func.sum(Record.amount)).filter(
        Record.user_id == user.id,
        Record.type == "income"
    ).scalar() or 0

    total_expense = db.query(func.sum(Record.amount)).filter(
        Record.user_id == user.id,
        Record.type == "expense"
    ).scalar() or 0

    net_balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }