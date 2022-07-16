from typing import List
from src.data.interfaces import UserRepositoryInterface
from src.domain.models import User
from src.domain.test import mock_user


class UserRepositorySpy(UserRepositoryInterface):
    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(
        self, name: str, email: str, password: str, phone_number: str, role: str
    ):
        self.insert_user_params["name"] = name
        self.insert_user_params["email"] = email
        self.insert_user_params["password"] = password
        self.insert_user_params["phone_number"] = phone_number
        self.insert_user_params["role"] = role

        return mock_user()

    def select_user(self, user_id: int = None, email: str = None) -> List[User]:
        self.select_user_params["user_id"] = user_id
        self.select_user_params["email"] = email

        return [mock_user()]
