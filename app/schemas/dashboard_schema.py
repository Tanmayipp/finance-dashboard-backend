from pydantic import BaseModel, Field
from decimal import Decimal


class SummaryResponse(BaseModel):
    total_income: Decimal = Field(..., example=50000)
    total_expense: Decimal = Field(..., example=30000)
    net_balance: Decimal = Field(..., example=20000)