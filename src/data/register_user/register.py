from typing import Type, Dict
from src.domain.models import User
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class RegisterUser(RegisterUserInterface):
    """Class to define use case: Register User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(
        self, name: str, email: str, password: str, phone_number: str, role: str
    ) -> Dict[bool, User]:
        """Register user use case"""
        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(email, str)
            and isinstance(phone_number, str)
            and isinstance(role, str)
        )

        if validate_entry:
            response = self.user_repository.insert_user(
                name, email, password, phone_number, role
            )

        return {"success": validate_entry, "data": response}
