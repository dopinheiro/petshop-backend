from faker import Faker
from .pet_repository import PetRepository
from src.domain import Pet
from src.infra.config import DBConnectionHandler
from datetime import date

faker = Faker()
db_connection = DBConnectionHandler()
pet_repository = PetRepository()
engine = db_connection.get_engine()


def test_insert_pet():
    name = faker.name()
    birth = date.today()
    note = faker.sentence(5)
    user_id = faker.random_number(digits=2)
    specie = "dog"

    test_insert = pet_repository.insert_pet(name, birth, note, specie, user_id)
    query_pet = engine.execute(
        f"SELECT * FROM pets WHERE id={test_insert.id}"
    ).fetchone()
    engine.execute(f"DELETE FROM pets WHERE id={test_insert.id}")

    assert test_insert == query_pet


def test_select_pet():
    pet_id = faker.random_number(digits=2)
    name = faker.name()
    birth = date.today()
    note = faker.sentence(5)
    user_id = faker.random_number(digits=2)
    specie = "dog"

    data = Pet(pet_id, name, birth, note, specie, user_id)

    engine.execute(
        f"""
        INSERT INTO pets (
            id, name, birth, note, specie, user_id)
        VALUES (
            {data.id}, '{data.name}', '{data.birth}',
            '{data.note}', '{data.specie}', '{data.user_id}')"""
    )

    test_select_pet_by_id = pet_repository.select_pet(pet_id=data.id)
    test_select_pet_by_user_id = pet_repository.select_pet(user_id=data.user_id)
    test_select_pet_by_id_and_user_id = pet_repository.select_pet(
        pet_id=data.id, user_id=data.user_id
    )
    engine.execute(f"DELETE FROM pets WHERE id={data.id}")

    assert data in test_select_pet_by_id
    assert data in test_select_pet_by_user_id
    assert data in test_select_pet_by_id_and_user_id
