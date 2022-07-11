from abc import ABC, abstractmethod
from src.domain.models import User
from typing import List, Dict


class FindUser(ABC):
    """Interface to FindUser user case"""

    @classmethod
    @abstractmethod
    def by_id(cls, user_id: str) -> Dict[bool, List[User]]:
        raise Exception("Should implement method: by_id")


"""
    @classmethod
    @abstractmethod
    def by_email(cls, email: str) -> Dict[bool, List[User]]:
        raise Exception("Should implement method: by_email")

    @classmethod
    @abstractmethod
    def by_id_and_email(cls, user_id: str, email: str) -> Dict[bool, List[User]]:
        raise Exception("Should implement method: by_id_and_email")
"""
