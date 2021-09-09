from abc import ABC, abstractmethod


class ABCParser(ABC):

    def __init__(self, file_uri: str) -> None:
        self.file_uri = file_uri

    @abstractmethod
    def get_parcels(self) -> list:
        pass