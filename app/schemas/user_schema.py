from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    viewer = "viewer"
    analyst = "analyst"
    admin = "admin"


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


# Base schema
class UserBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr


# Create user
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)
    role: UserRole


# Update user
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    role: Optional[UserRole]
    status: Optional[UserStatus]


# Response
class UserResponse(UserBase):
    id: int
    role: UserRole
    status: UserStatus

    class Config:
        from_attributes = True