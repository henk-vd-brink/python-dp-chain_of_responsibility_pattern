from .base_department import BaseDepartment


class MailDepartment(BaseDepartment):
    def can_handle(self, parcel):
        return parcel.weight < 1

    def handle_parcel(self, parcel):
        print("Handled by mail department")
