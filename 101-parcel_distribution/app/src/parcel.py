from dataclasses import dataclass

@dataclass
class ReceipientInfo:
    name: str
    street: str
    house_number: str
    postal_code: str
    city: str

@dataclass
class ParcelInfo:
    weight: float
    value: float

@dataclass
class Parcel(ParcelInfo):
    receipient_info: ReceipientInfo






