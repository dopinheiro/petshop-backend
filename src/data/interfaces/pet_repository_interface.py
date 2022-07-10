from abc import ABC, abstractmethod
from typing import List, Any
from src.domain.models import Pet


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_pet(
        self, name: str, birth: Any, note: str, specie: str, user_id: int
    ) -> Pet:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pet]:
        """abstractmethod"""

        raise Exception("Method not implemented")
