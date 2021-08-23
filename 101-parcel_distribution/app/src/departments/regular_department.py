from .department import Department

class RegularDepartment(Department):

    def can_handle(self, parcel):
        return (parcel.weight < 10)

    def handle_parcel(self, parcel):
        print("Handled by regular department")