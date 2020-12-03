from datetime import datetime
from uuid import UUID

import attr

__all__ = (
    "Account",
    "LoginResponse",
    "Password",
)


@attr.s(auto_attribs=True, slots=True, frozen=True)
class Account:
    id: UUID
    first_name: str
    last_name: str
    balance: int
    email: str
    password: bytes
    created_at: datetime


@attr.s(auto_attribs=True, slots=True, frozen=True)
class LoginResponse:
    id: UUID
    token: str


@attr.s(auto_attribs=True, slots=True, frozen=True)
class Password:
    id: UUID
    salt: bytes
    password: bytes
    created_at: datetime