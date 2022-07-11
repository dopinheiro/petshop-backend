from faker import Faker
from src.domain.models import User

faker = Faker()


def mock_user() -> User:
    """Mocking Users"""

    return User(
        id=faker.random_number(digits=5),
        name=faker.name(),
        email=faker.email(),
        password=faker.name(),
        phone_number=faker.phone_number(),
        role="admin",
    )
