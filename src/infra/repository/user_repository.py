from src.domain.models import User
from src.infra.config import DBConnectionHandler
from src.infra.entities import User as UserModel
from src.data.interfaces import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    """Class to manage users table"""

    @classmethod
    def insert_user(cls, name, email, password, phone_number, role):
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserModel(
                    name=name,
                    email=email,
                    password=password,
                    phone_number=phone_number,
                    role=role,
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return User(new_user.id, name, email, password, phone_number, role)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_user(
        cls,
        user_id: int = None,
        email: str = None,
    ):
        with DBConnectionHandler() as db_connection:
            query_data = []
            try:
                data = db_connection.session.query(UserModel)
                if user_id and not email:
                    query_data.append(data.filter_by(id=user_id).one_or_none())
                elif email and not user_id:
                    query_data.append(data.filter_by(email=email).one_or_none())
                elif user_id and email:
                    query_data.append(
                        data.filter_by(id=user_id, email=email).one_or_none()
                    )

                return query_data
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
