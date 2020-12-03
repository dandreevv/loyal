from abc import ABC, abstractmethod

__all__ = (
    "UserRepositoryInterface",
    "PasswordRepositoryInterface",
)

from datetime import datetime
from typing import Optional

from uuid import UUID

from .entities import Account, Password


class UserRepositoryInterface(ABC):

    @abstractmethod
    async def add(
        self,
        uid: UUID,
        first_name: str,
        last_name: str,
        email: str,
        password_id: UUID,
        balance: float,
        created_at: datetime,
    ):
        pass

    @abstractmethod
    async def find_by_id(self, uid: UUID) -> Optional[Account]:
        pass

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[Account]:
        pass


class PasswordRepositoryInterface(ABC):

    @abstractmethod
    async def add(
        self,
        pid: UUID,
        salt: bytes,
        password: bytes,
        created_at: datetime,
    ):
        pass

    @abstractmethod
    async def find(self, password_id: UUID) -> Password:
        pass
