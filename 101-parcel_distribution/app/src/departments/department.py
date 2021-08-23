from .abc_department import ABCDepartment

class Department(ABCDepartment):

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






    
