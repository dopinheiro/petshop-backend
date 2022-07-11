from typing import Type, Dict, List

from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.use_cases import FindUser as FindUserInterface
from src.domain.models import User


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[User]]:
        """Select user by id
        :param - user_id: id of user
        :returns -"""
        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"success": validate_entry, "data": response}

    def by_email(self, email: str) -> Dict[bool, List[User]]:
        """Select user by id
        :param - email: email of user
        :returns -"""
        response = None

        validate_entry = isinstance(email, str)

        if validate_entry:
            response = self.user_repository.select_user(email=email)

        return {"success": validate_entry, "data": response}
