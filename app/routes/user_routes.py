from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.record_schema import RecordCreate, RecordResponse
from app.core.security import role_required
from app.services import record_service

router = APIRouter(prefix="/records", tags=["Records"])


@router.post("/", response_model=RecordResponse)
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["admin"]))
):
    return record_service.create_record(db, user, record)