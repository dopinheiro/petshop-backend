from faker import Faker
from .register import RegisterUser
from src.infra.test.user_repository_spy import UserRepositorySpy

faker = Faker()


def test_register():
    """Assert if can register user"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "phone_number": faker.phone_number(),
        "role": "admin",
    }

    response = register_user.register(
        name=attributes["name"],
        email=attributes["email"],
        password=attributes["password"],
        phone_number=attributes["phone_number"],
        role="admin",
    )

    assert user_repo.insert_user_params == attributes
    assert response["success"]
    assert response["data"]


def test_register_error():
    """Assert register user in fail"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.random_number(),
        "email": faker.email(),
        "password": faker.password(),
        "phone_number": faker.phone_number(),
        "role": "admin",
    }

    response = register_user.register(
        name=attributes["name"],
        email=attributes["email"],
        password=attributes["password"],
        phone_number=attributes["phone_number"],
        role="admin",
    )

    assert user_repo.insert_user_params == {}
    assert not response["success"]
    assert not response["data"]
