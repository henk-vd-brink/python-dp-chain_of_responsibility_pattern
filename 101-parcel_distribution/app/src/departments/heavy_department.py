from .department import Department

class HeavyDepartment(Department):

    def can_handle(self, parcel):
        return (parcel.weight > 10)

    def handle_parcel(self, parcel):
        print("Handled by heavy department")