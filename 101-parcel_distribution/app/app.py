from src.departments import (  MailDepartment, 
                    RegularDepartment,
                    HeavyDepartment )
from src.parcel import Parcel
from abc import ABC, abstractmethod

class BuildChain(ABC):
    
    def __init__(self, *args, **kwargs):
        self._chain = self._build_chain()
    
    @abstractmethod
    def _build_chain(self):
        pass

    @property
    def chain(self):
        return self._chain

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


if __name__ == "__main__":
    chain = BuildChainCompanyA().chain
    parcels = [Parcel(weight=0.5), Parcel(weight=8), Parcel(weight=11)]

    for parcel in parcels:
        chain.handle(parcel)