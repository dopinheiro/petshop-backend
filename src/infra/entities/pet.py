import enum

from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey
from src.infra.config import Base


class PetTypes(enum.Enum):
    """Define animal types"""

    dog = "dog"
    cat = "dog"


class Pet(Base):
    """Pet Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    birth = Column(Date, nullable=False)
    note = Column(String(80), nullable=False)
    specie = Column(Enum(PetTypes), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return f"Pet [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.birth == other.birth
            and self.note == other.note
            and self.specie.value == other.specie
            and self.user_id == other.user_id
        ):
            return True
        else:
            return False
