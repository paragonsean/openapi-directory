# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.geo_code import GeoCode
from openapi_server.models.links import Links
from openapi_server import util


class Location(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, geo_code: GeoCode=None, id: str=None, name: str=None, _self: Links=None, sub_type: str=None, type: str=None):
        """Location - a model defined in OpenAPI

        :param geo_code: The geo_code of this Location.
        :param id: The id of this Location.
        :param name: The name of this Location.
        :param _self: The _self of this Location.
        :param sub_type: The sub_type of this Location.
        :param type: The type of this Location.
        """
        self.openapi_types = {
            'geo_code': GeoCode,
            'id': str,
            'name': str,
            '_self': Links,
            'sub_type': str,
            'type': str
        }

        self.attribute_map = {
            'geo_code': 'geoCode',
            'id': 'id',
            'name': 'name',
            '_self': 'self',
            'sub_type': 'subType',
            'type': 'type'
        }

        self._geo_code = geo_code
        self._id = id
        self._name = name
        self.__self = _self
        self._sub_type = sub_type
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Location':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Location of this Location.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def geo_code(self):
        """Gets the geo_code of this Location.


        :return: The geo_code of this Location.
        :rtype: GeoCode
        """
        return self._geo_code

    @geo_code.setter
    def geo_code(self, geo_code):
        """Sets the geo_code of this Location.


        :param geo_code: The geo_code of this Location.
        :type geo_code: GeoCode
        """

        self._geo_code = geo_code

    @property
    def id(self):
        """Gets the id of this Location.

        id of the ressource

        :return: The id of this Location.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.

        id of the ressource

        :param id: The id of this Location.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Location.

        short name of the location

        :return: The name of this Location.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Location.

        short name of the location

        :param name: The name of this Location.
        :type name: str
        """

        self._name = name

    @property
    def _self(self):
        """Gets the _self of this Location.


        :return: The _self of this Location.
        :rtype: Links
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Location.


        :param _self: The _self of this Location.
        :type _self: Links
        """

        self.__self = _self

    @property
    def sub_type(self):
        """Gets the sub_type of this Location.

        location sub type

        :return: The sub_type of this Location.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this Location.

        location sub type

        :param sub_type: The sub_type of this Location.
        :type sub_type: str
        """
        allowed_values = ["AIRPORT", "CITY", "POINT_OF_INTEREST", "DISTRICT"]  # noqa: E501
        if sub_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_type` ({0}), must be one of {1}"
                .format(sub_type, allowed_values)
            )

        self._sub_type = sub_type

    @property
    def type(self):
        """Gets the type of this Location.

        the resource name

        :return: The type of this Location.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Location.

        the resource name

        :param type: The type of this Location.
        :type type: str
        """

        self._type = type
