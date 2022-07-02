from src.domain import Pet
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pet as PetModel


class PetRepository:
    """Class to manage pets table"""

    @classmethod
    def insert_pet(cls, name, birth, note, specie, user_id):
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetModel(
                    name=name, birth=birth, note=note, specie=specie, user_id=user_id
                )
                db_connection.session.add(new_pet)
                db_connection.session.commit()
                return Pet(
                    new_pet.id,
                    name,
                    new_pet.birth.strftime("%Y-%m-%d"),
                    note,
                    specie,
                    user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None):
        with DBConnectionHandler() as db_connection:
            query_data = []
            try:
                data = db_connection.session.query(PetModel)
                if pet_id and not user_id:
                    query_data.append(data.filter_by(id=pet_id).one_or_none())
                elif user_id and not pet_id:
                    query_data = data.filter_by(user_id=user_id).all()
                elif pet_id and user_id:
                    query_data.append(
                        data.filter_by(id=pet_id, user_id=user_id).one_or_none()
                    )
                return query_data
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
