import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Database connection handler"""

    def __init__(self):
        self.__connection_string = os.getenv("CONNECTION_STR")

    def get_engine(self):
        """Return connection engine
        :param - None
        :return - sqlalchemy engine"""
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
