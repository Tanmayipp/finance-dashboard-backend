from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.database import get_db
from app.schemas.record_schema import (
    RecordCreate,
    RecordResponse,
    RecordUpdate
)
from app.core.security import role_required
from app.services import record_service

router = APIRouter(prefix="/records", tags=["Records"])


# CREATE
@router.post("/", response_model=RecordResponse)
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):
    return record_service.create_record(db, user, record)


# GET (with filtering)
@router.get("/", response_model=list[RecordResponse])
def get_records(
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    user=Depends(role_required(["analyst", "admin"]))
):
    return record_service.get_records(
        db=db,
        user=user,
        type=type,
        category=category,
        start_date=start_date,
        end_date=end_date
    )


# UPDATE
@router.put("/{record_id}", response_model=RecordResponse)
def update_record(
    record_id: int,
    record: RecordUpdate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):
    updated_record = record_service.update_record(db, user, record_id, record)

    if not updated_record:
        raise HTTPException(status_code=404, detail="Record not found")

    return updated_record


# DELETE
@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):
    success = record_service.delete_record(db, user, record_id)

    if not success:
        raise HTTPException(status_code=404, detail="Record not found")

    return {"message": "Record deleted successfully"}