# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Location(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, lat: float=None, lon: float=None, name: str=None):
        """Location - a model defined in OpenAPI

        :param id: The id of this Location.
        :param lat: The lat of this Location.
        :param lon: The lon of this Location.
        :param name: The name of this Location.
        """
        self.openapi_types = {
            'id': str,
            'lat': float,
            'lon': float,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'lat': 'lat',
            'lon': 'lon',
            'name': 'name'
        }

        self._id = id
        self._lat = lat
        self._lon = lon
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Location':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Location of this Location.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Location.

        id of location (eva-number), example: 8000105

        :return: The id of this Location.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.

        id of location (eva-number), example: 8000105

        :param id: The id of this Location.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def lat(self):
        """Gets the lat of this Location.

        latitude, example: 50.107149

        :return: The lat of this Location.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Location.

        latitude, example: 50.107149

        :param lat: The lat of this Location.
        :type lat: float
        """
        if lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Location.

        longitude, example: 8.663785

        :return: The lon of this Location.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Location.

        longitude, example: 8.663785

        :param lon: The lon of this Location.
        :type lon: float
        """
        if lon is None:
            raise ValueError("Invalid value for `lon`, must not be `None`")

        self._lon = lon

    @property
    def name(self):
        """Gets the name of this Location.

        Name of location, example: Frankfurt(Main)Hbf

        :return: The name of this Location.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Location.

        Name of location, example: Frankfurt(Main)Hbf

        :param name: The name of this Location.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
