from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from enum import Enum
from decimal import Decimal


class RecordType(str, Enum):
    income = "income"
    expense = "expense"


class RecordBase(BaseModel):
    amount: Decimal = Field(..., gt=0, example=1000)
    type: RecordType
    category: str = Field(..., min_length=1, example="Food")
    date: date


class RecordCreate(RecordBase):
    notes: Optional[str] = None


class RecordUpdate(BaseModel):
    amount: Optional[Decimal] = Field(None, gt=0)
    type: Optional[RecordType]
    category: Optional[str] = Field(None, min_length=1)
    date: Optional[date]
    notes: Optional[str]


class RecordResponse(RecordBase):
    id: int
    notes: Optional[str]

    class Config:
        from_attributes = True