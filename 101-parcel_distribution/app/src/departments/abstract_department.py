from abc import ABC, abstractmethod

class Department(ABC):

    @property
    def successor(self):
        return self._successor

    @successor.setter
    def successor(self, successor):
        self._successor = successor

    def handle(self, parcel):
        if self.can_handle(parcel):
            self.handle_parcel(parcel)
        elif self._successor:
            self._successor.handle(parcel)
        else:
            raise NotImplementedError

    @abstractmethod
    def can_handle(self, parcel):
        pass

    @abstractmethod
    def handle_parcel(self, parcel):
        pass





    
