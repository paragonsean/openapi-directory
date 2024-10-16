# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DistrictList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, abbreviation: str=None, display_name: str=None, key: str=None, year: int=None):
        """DistrictList - a model defined in OpenAPI

        :param abbreviation: The abbreviation of this DistrictList.
        :param display_name: The display_name of this DistrictList.
        :param key: The key of this DistrictList.
        :param year: The year of this DistrictList.
        """
        self.openapi_types = {
            'abbreviation': str,
            'display_name': str,
            'key': str,
            'year': int
        }

        self.attribute_map = {
            'abbreviation': 'abbreviation',
            'display_name': 'display_name',
            'key': 'key',
            'year': 'year'
        }

        self._abbreviation = abbreviation
        self._display_name = display_name
        self._key = key
        self._year = year

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DistrictList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The District_List of this DistrictList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def abbreviation(self):
        """Gets the abbreviation of this DistrictList.

        The short identifier for the district.

        :return: The abbreviation of this DistrictList.
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this DistrictList.

        The short identifier for the district.

        :param abbreviation: The abbreviation of this DistrictList.
        :type abbreviation: str
        """
        if abbreviation is None:
            raise ValueError("Invalid value for `abbreviation`, must not be `None`")

        self._abbreviation = abbreviation

    @property
    def display_name(self):
        """Gets the display_name of this DistrictList.

        The long name for the district.

        :return: The display_name of this DistrictList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DistrictList.

        The long name for the district.

        :param display_name: The display_name of this DistrictList.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name

    @property
    def key(self):
        """Gets the key of this DistrictList.

        Key for this district, e.g. `2016ne`.

        :return: The key of this DistrictList.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DistrictList.

        Key for this district, e.g. `2016ne`.

        :param key: The key of this DistrictList.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def year(self):
        """Gets the year of this DistrictList.

        Year this district participated.

        :return: The year of this DistrictList.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this DistrictList.

        Year this district participated.

        :param year: The year of this DistrictList.
        :type year: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")

        self._year = year
