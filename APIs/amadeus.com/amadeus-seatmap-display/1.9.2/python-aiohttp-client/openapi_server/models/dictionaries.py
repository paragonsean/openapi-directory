# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.location_value import LocationValue
from openapi_server import util


class Dictionaries(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, facilities: Dict[str, str]=None, locations: Dict[str, LocationValue]=None, seat_characteristics: Dict[str, str]=None):
        """Dictionaries - a model defined in OpenAPI

        :param facilities: The facilities of this Dictionaries.
        :param locations: The locations of this Dictionaries.
        :param seat_characteristics: The seat_characteristics of this Dictionaries.
        """
        self.openapi_types = {
            'facilities': Dict[str, str],
            'locations': Dict[str, LocationValue],
            'seat_characteristics': Dict[str, str]
        }

        self.attribute_map = {
            'facilities': 'facilities',
            'locations': 'locations',
            'seat_characteristics': 'seatCharacteristics'
        }

        self._facilities = facilities
        self._locations = locations
        self._seat_characteristics = seat_characteristics

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Dictionaries':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Dictionaries of this Dictionaries.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def facilities(self):
        """Gets the facilities of this Dictionaries.

        on board facilities map. E.g: bulkhead, closet, exit door, galley, lavatory

        :return: The facilities of this Dictionaries.
        :rtype: Dict[str, str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this Dictionaries.

        on board facilities map. E.g: bulkhead, closet, exit door, galley, lavatory

        :param facilities: The facilities of this Dictionaries.
        :type facilities: Dict[str, str]
        """

        self._facilities = facilities

    @property
    def locations(self):
        """Gets the locations of this Dictionaries.


        :return: The locations of this Dictionaries.
        :rtype: Dict[str, LocationValue]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this Dictionaries.


        :param locations: The locations of this Dictionaries.
        :type locations: Dict[str, LocationValue]
        """

        self._locations = locations

    @property
    def seat_characteristics(self):
        """Gets the seat_characteristics of this Dictionaries.

        seat characteristics dictionary allows mapping a service characteristic to its name. Possible values are part of:   IATA code: Most of the codes are defined by IATA Standard/IATA Code list 9825, Example: CH = Chargeable Seat, W = Window Seat, A = Aisle              Seat, Q = Seat in a quiet zone, E = Exit Row Seat   Amadeus Code: defined as extension, example MV=row with movie screen   Seat map display Code: API specific codes, example 1A_AQC_PREMIUM_SEAT=premium seat

        :return: The seat_characteristics of this Dictionaries.
        :rtype: Dict[str, str]
        """
        return self._seat_characteristics

    @seat_characteristics.setter
    def seat_characteristics(self, seat_characteristics):
        """Sets the seat_characteristics of this Dictionaries.

        seat characteristics dictionary allows mapping a service characteristic to its name. Possible values are part of:   IATA code: Most of the codes are defined by IATA Standard/IATA Code list 9825, Example: CH = Chargeable Seat, W = Window Seat, A = Aisle              Seat, Q = Seat in a quiet zone, E = Exit Row Seat   Amadeus Code: defined as extension, example MV=row with movie screen   Seat map display Code: API specific codes, example 1A_AQC_PREMIUM_SEAT=premium seat

        :param seat_characteristics: The seat_characteristics of this Dictionaries.
        :type seat_characteristics: Dict[str, str]
        """

        self._seat_characteristics = seat_characteristics
