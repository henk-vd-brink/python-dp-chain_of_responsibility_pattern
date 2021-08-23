from .department import Department

class MailDepartment(Department):

    def can_handle(self, parcel):
        return (parcel.weight < 1)

    def handle_parcel(self, parcel):
        print("Handled by mail department")
            