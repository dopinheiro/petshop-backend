from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import User


class RegisterUser(ABC):
    """Interface to RegisterUser case"""

    @classmethod
    @abstractmethod
    def register(
        cls, name: str, email: str, password: str, phone_number: str, role: str
    ) -> Dict[bool, User]:
        """Case"""

        raise Exception("Should implement this method")
