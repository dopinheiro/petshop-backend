from abc import ABC
from typing import Dict
from src.domain.models import User


class RegisterUser(ABC):
    """Interface to RegisterUser case"""

    @classmethod
    def register(
        cls, name: str, email: str, password: str, phone_number: str, role: str
    ) -> Dict[bool, User]:
        """Case"""

        raise Exception("Should implement this method")
