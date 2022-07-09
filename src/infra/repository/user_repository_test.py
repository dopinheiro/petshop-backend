from faker import Faker
from .user_repository import UserRepository
from src.domain.models import User
from src.infra.config import DBConnectionHandler

faker = Faker()
db_connection = DBConnectionHandler()
user_repository = UserRepository()
engine = db_connection.get_engine()


def test_insert_user():
    name = faker.name()
    email = faker.email()
    password = faker.password()
    phone_number = faker.phone_number()
    role = "admin"

    test_insert = user_repository.insert_user(name, email, password, phone_number, role)
    query_user = engine.execute(
        f"SELECT * FROM users WHERE id={test_insert.id}"
    ).fetchone()
    engine.execute(f"DELETE FROM users WHERE id={test_insert.id}")

    assert test_insert == query_user


def test_select_user():
    id = faker.random_number(digits=2)
    name = faker.name()
    email = faker.email()
    password = faker.password()
    phone_number = faker.phone_number()
    role = "admin"

    data = User(id, name, email, password, phone_number, role)

    engine.execute(
        f"""
        INSERT INTO users (
            id, name, email, password, phone_number, role)
        VALUES (
            {data.id}, '{data.name}', '{data.email}',
            '{data.password}', '{data.phone_number}', '{data.role}')"""
    )

    test_select_user_by_id = user_repository.select_user(user_id=data.id)
    test_select_user_by_email = user_repository.select_user(email=data.email)
    test_select_user_by_id_and_email = user_repository.select_user(
        user_id=data.id, email=data.email
    )

    assert data in test_select_user_by_id
    assert data in test_select_user_by_email
    assert data in test_select_user_by_id_and_email

    engine.execute(f"DELETE FROM users WHERE id={data.id}")
