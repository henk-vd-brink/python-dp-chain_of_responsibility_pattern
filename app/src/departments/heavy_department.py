from .abc_department import ABCDepartment

class HeavyDepartment(ABCDepartment):

    def can_handle(self, parcel):
        return (parcel.weight >= 10)

    def handle_parcel(self, parcel):
        print("Handled by heavy department")