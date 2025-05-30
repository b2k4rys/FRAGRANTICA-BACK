# src/schemas/user.py
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from backend.core.db.models.user import Role

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Role = Role.USER

class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def password_strength(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        return value

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

