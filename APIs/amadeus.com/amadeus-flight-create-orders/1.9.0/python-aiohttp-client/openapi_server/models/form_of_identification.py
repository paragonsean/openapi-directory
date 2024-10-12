# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FormOfIdentification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, carrier_code: str=None, flight_offer_ids: List[str]=None, identification_type: str=None, number: str=None, traveler_ids: List[str]=None):
        """FormOfIdentification - a model defined in OpenAPI

        :param carrier_code: The carrier_code of this FormOfIdentification.
        :param flight_offer_ids: The flight_offer_ids of this FormOfIdentification.
        :param identification_type: The identification_type of this FormOfIdentification.
        :param number: The number of this FormOfIdentification.
        :param traveler_ids: The traveler_ids of this FormOfIdentification.
        """
        self.openapi_types = {
            'carrier_code': str,
            'flight_offer_ids': List[str],
            'identification_type': str,
            'number': str,
            'traveler_ids': List[str]
        }

        self.attribute_map = {
            'carrier_code': 'carrierCode',
            'flight_offer_ids': 'flightOfferIds',
            'identification_type': 'identificationType',
            'number': 'number',
            'traveler_ids': 'travelerIds'
        }

        self._carrier_code = carrier_code
        self._flight_offer_ids = flight_offer_ids
        self._identification_type = identification_type
        self._number = number
        self._traveler_ids = traveler_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FormOfIdentification':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FormOfIdentification of this FormOfIdentification.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def carrier_code(self):
        """Gets the carrier_code of this FormOfIdentification.

        providing the airline / carrier code

        :return: The carrier_code of this FormOfIdentification.
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this FormOfIdentification.

        providing the airline / carrier code

        :param carrier_code: The carrier_code of this FormOfIdentification.
        :type carrier_code: str
        """
        if carrier_code is not None and len(carrier_code) > 2:
            raise ValueError("Invalid value for `carrier_code`, length must be less than or equal to `2`")
        if carrier_code is not None and len(carrier_code) < 1:
            raise ValueError("Invalid value for `carrier_code`, length must be greater than or equal to `1`")

        self._carrier_code = carrier_code

    @property
    def flight_offer_ids(self):
        """Gets the flight_offer_ids of this FormOfIdentification.

        Id of the concerned flightOffers

        :return: The flight_offer_ids of this FormOfIdentification.
        :rtype: List[str]
        """
        return self._flight_offer_ids

    @flight_offer_ids.setter
    def flight_offer_ids(self, flight_offer_ids):
        """Sets the flight_offer_ids of this FormOfIdentification.

        Id of the concerned flightOffers

        :param flight_offer_ids: The flight_offer_ids of this FormOfIdentification.
        :type flight_offer_ids: List[str]
        """
        if flight_offer_ids is not None and len(flight_offer_ids) > 6:
            raise ValueError("Invalid value for `flight_offer_ids`, number of items must be less than or equal to `6`")
        if flight_offer_ids is not None and len(flight_offer_ids) < 1:
            raise ValueError("Invalid value for `flight_offer_ids`, number of items must be greater than or equal to `1`")

        self._flight_offer_ids = flight_offer_ids

    @property
    def identification_type(self):
        """Gets the identification_type of this FormOfIdentification.

        Type of identification

        :return: The identification_type of this FormOfIdentification.
        :rtype: str
        """
        return self._identification_type

    @identification_type.setter
    def identification_type(self, identification_type):
        """Sets the identification_type of this FormOfIdentification.

        Type of identification

        :param identification_type: The identification_type of this FormOfIdentification.
        :type identification_type: str
        """
        allowed_values = ["DRIVERS_LICENSE", "PASSPORT", "NATIONAL_IDENTITY_CARD", "BOOKING_CONFIRMATION", "TICKET", "OTHER_ID"]  # noqa: E501
        if identification_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identification_type` ({0}), must be one of {1}"
                .format(identification_type, allowed_values)
            )

        self._identification_type = identification_type

    @property
    def number(self):
        """Gets the number of this FormOfIdentification.

        identification number relative to the type of identification either ticket number, booking number, passport number, identity card number, drivers licence number, other ID

        :return: The number of this FormOfIdentification.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this FormOfIdentification.

        identification number relative to the type of identification either ticket number, booking number, passport number, identity card number, drivers licence number, other ID

        :param number: The number of this FormOfIdentification.
        :type number: str
        """

        self._number = number

    @property
    def traveler_ids(self):
        """Gets the traveler_ids of this FormOfIdentification.

        Ids of the concerned travelers

        :return: The traveler_ids of this FormOfIdentification.
        :rtype: List[str]
        """
        return self._traveler_ids

    @traveler_ids.setter
    def traveler_ids(self, traveler_ids):
        """Sets the traveler_ids of this FormOfIdentification.

        Ids of the concerned travelers

        :param traveler_ids: The traveler_ids of this FormOfIdentification.
        :type traveler_ids: List[str]
        """

        self._traveler_ids = traveler_ids
