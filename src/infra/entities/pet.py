import enum

from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey
from src.infra.config import Base


class PetTypes(enum.Enum):
    """Define animal types"""

    dog = {1: "cachorro"}
    cat = {2: "gato"}


class Pet(Base):
    """Pet Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    birth = Column(DateTime, nullable=False)
    note = Column(String(80), nullable=False)
    specie = Column(Enum(PetTypes), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return f"Usr [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.birth == other.birth
            and self.note == other.note
            and self.specie == other.specie
            and self.user_id == other.user_id
        ):
            return True
        else:
            return False
