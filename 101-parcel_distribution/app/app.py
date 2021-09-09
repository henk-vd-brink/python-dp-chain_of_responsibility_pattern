from src import (   Parcel, 
                    ABCBuildChain,
                    XmlParser,
                    MailDepartment, 
                    RegularDepartment,
                    HeavyDepartment )

FILE_URI = "app/data/parcels.xml"
parser = XmlParser(file_uri=FILE_URI)

class BuildChainCompanyA(ABCBuildChain):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _build_chain(self):
        mail_department = MailDepartment()
        regular_department = RegularDepartment()
        heavy_department = HeavyDepartment()

        mail_department.successor = regular_department
        regular_department.successor = heavy_department
        return mail_department


def run():
    parcels = parser.get_parcels()
    chain = BuildChainCompanyA().chain

    for parcel in parcels:
        chain.handle(parcel)