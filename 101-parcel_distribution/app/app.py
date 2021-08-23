from src import (   Parcel, 
                    BuildChain,
                    MailDepartment, 
                    RegularDepartment,
                    HeavyDepartment )
from abc import ABC, abstractmethod

class BuildChainCompanyA(BuildChain):
    
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
    chain = BuildChainCompanyA().chain
    parcels = [Parcel(weight=0.5), Parcel(weight=8), Parcel(weight=11)]

    for parcel in parcels:
        chain.handle(parcel)