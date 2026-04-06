from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import role_required
from app.schemas.dashboard_schema import SummaryResponse
from app.services import dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary", response_model=SummaryResponse)
def get_summary(
    db: Session = Depends(get_db),
    user=Depends(role_required(["analyst", "admin"]))
):
    return dashboard_service.get_summary(db, user)