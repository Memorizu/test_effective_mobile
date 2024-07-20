from abc import ABC, abstractmethod


class DataManager(ABC):

    @abstractmethod
    def load_data(self) -> list:
        pass

    @abstractmethod
    def save_data(self, data: list) -> None:
        pass
