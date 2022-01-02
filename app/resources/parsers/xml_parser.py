import os.path
from xml.etree import ElementTree
from ..parcel import Parcel, ParcelInfo, ReceipientInfo
from dataclasses import asdict
from .base_parser import BaseParser


class XmlParser(BaseParser):
    def __init__(self, file_uri: str) -> None:
        super().__init__(file_uri)

    def _parse_file(self) -> list:
        if os.path.exists(self.file_uri):
            parsed_file = ElementTree.parse(self.file_uri)
            xml_parcels = parsed_file.findall("./parcels/Parcel")
            return xml_parcels
        else:
            return []

    def _parse_xml_parcel_receipient_info(self, xml_parcel: str) -> ReceipientInfo:
        name = xml_parcel.find("./Receipient/Name").text
        street = xml_parcel.find("./Receipient/Address/Street").text
        house_number = xml_parcel.find("./Receipient/Address/HouseNumber").text
        postal_code = xml_parcel.find("./Receipient/Address/PostalCode").text
        city = xml_parcel.find("./Receipient/Address/City").text
        return ReceipientInfo(
            name=name,
            street=street,
            house_number=house_number,
            postal_code=postal_code,
            city=city,
        )

    def _parse_xml_parcel_info(self, xml_parcel: str) -> ParcelInfo:
        weight = float(xml_parcel.find("Weight").text)
        value = xml_parcel.find("Value").text
        return ParcelInfo(weight=weight, value=value)

    def _build_parcel_object(
        self, parcel_info: ParcelInfo, receipient_info: ReceipientInfo
    ) -> Parcel:
        return Parcel(**asdict(parcel_info), receipient_info=receipient_info)

    def get_parcels(self) -> list:
        xml_parcels = self._parse_file()

        if not xml_parcels:
            return []

        list_parsed_parcels = []
        for xml_parcel in xml_parcels:
            receipient_info = self._parse_xml_parcel_receipient_info(
                xml_parcel=xml_parcel
            )
            parcel_info = self._parse_xml_parcel_info(xml_parcel=xml_parcel)
            parcel = self._build_parcel_object(parcel_info, receipient_info)
            list_parsed_parcels.append(parcel)
        return list_parsed_parcels
