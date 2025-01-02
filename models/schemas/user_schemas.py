from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    email: str = Field(..., example="example@example.com")
    password: str = Field(..., min_length=6, example="yourpassword")

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int = Field(..., example=1)
    email: str = Field(..., example="example@example.com")
    created_date: datetime = Field(..., example="2023-01-01T00:00:00")
    updated_date: datetime = Field(..., example="2023-01-02T00:00:00")
    is_blocked: bool = Field(..., example=False)

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str = Field(..., example="example@example.com")
    password: str = Field(..., min_length=6, example="yourpassword")

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1...")
    token_type: str = Field("bearer", example="bearer")