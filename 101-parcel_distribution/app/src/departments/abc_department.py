from abc import ABC, abstractmethod

class ABCDepartment(ABC):
    
    @property
    @abstractmethod
    def successor(self):
        pass

    @successor.setter
    @abstractmethod
    def successor(self, successor):
        pass

    @abstractmethod
    def handle(self, parcel):
        pass

    @abstractmethod
    def can_handle(self, parcel):
        pass

    @abstractmethod
    def handle_parcel(self, parcel):
        pass
