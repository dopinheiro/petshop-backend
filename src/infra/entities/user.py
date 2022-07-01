import enum

from sqlalchemy import Column, String, Integer, Enum
from src.infra.config import Base


class RoleTypes(enum.Enum):
    """Define role types"""

    admin = {"id": 1, "name": "admin"}
    receptionist = {"id": 2, "name": "recepcionista"}
    groomer = {"id": 3, "name": "tosador"}
    client = {"id": 4, "name": "cliente"}


class User(Base):
    """User Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    password = Column(String(94), nullable=False)
    phone_number = Column(String(80), nullable=False)
    role = Column(Enum(RoleTypes), nullable=False)

    def __rep__(self):
        return f"Usr [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.email == other.email
            and self.password == other.password
            and self.phone_number == other.phone_number
            and self.role.value["name"] == other.role
        ):
            return True
        else:
            print(self.role.value)
            return False
