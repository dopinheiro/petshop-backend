from abc import ABC, abstractmethod
from typing import List
from src.domain.models import User


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(
        self, name: str, email: str, password: str, phone_number: str, role: str
    ) -> User:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, email: str = None) -> List[User]:
        """abstractmethod"""

        raise Exception("Method not implemented")
