# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.amenity_type import AmenityType
from openapi_server import util


class Amenity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amenity_type: AmenityType=None, code: str=None, description: str=None, is_chargeable: bool=None):
        """Amenity - a model defined in OpenAPI

        :param amenity_type: The amenity_type of this Amenity.
        :param code: The code of this Amenity.
        :param description: The description of this Amenity.
        :param is_chargeable: The is_chargeable of this Amenity.
        """
        self.openapi_types = {
            'amenity_type': AmenityType,
            'code': str,
            'description': str,
            'is_chargeable': bool
        }

        self.attribute_map = {
            'amenity_type': 'amenityType',
            'code': 'code',
            'description': 'description',
            'is_chargeable': 'isChargeable'
        }

        self._amenity_type = amenity_type
        self._code = code
        self._description = description
        self._is_chargeable = is_chargeable

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Amenity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Amenity of this Amenity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amenity_type(self):
        """Gets the amenity_type of this Amenity.


        :return: The amenity_type of this Amenity.
        :rtype: AmenityType
        """
        return self._amenity_type

    @amenity_type.setter
    def amenity_type(self, amenity_type):
        """Sets the amenity_type of this Amenity.


        :param amenity_type: The amenity_type of this Amenity.
        :type amenity_type: AmenityType
        """

        self._amenity_type = amenity_type

    @property
    def code(self):
        """Gets the code of this Amenity.


        :return: The code of this Amenity.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Amenity.


        :param code: The code of this Amenity.
        :type code: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this Amenity.


        :return: The description of this Amenity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Amenity.


        :param description: The description of this Amenity.
        :type description: str
        """

        self._description = description

    @property
    def is_chargeable(self):
        """Gets the is_chargeable of this Amenity.


        :return: The is_chargeable of this Amenity.
        :rtype: bool
        """
        return self._is_chargeable

    @is_chargeable.setter
    def is_chargeable(self, is_chargeable):
        """Sets the is_chargeable of this Amenity.


        :param is_chargeable: The is_chargeable of this Amenity.
        :type is_chargeable: bool
        """

        self._is_chargeable = is_chargeable
