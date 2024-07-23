from abc import ABC, abstractmethod


class LibraryItem(ABC):

    @abstractmethod
    def generate_id(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
