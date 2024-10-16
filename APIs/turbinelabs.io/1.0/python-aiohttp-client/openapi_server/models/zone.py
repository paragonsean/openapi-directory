# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Zone(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, checksum: str=None, name: str=None, zone_key: str=None):
        """Zone - a model defined in OpenAPI

        :param checksum: The checksum of this Zone.
        :param name: The name of this Zone.
        :param zone_key: The zone_key of this Zone.
        """
        self.openapi_types = {
            'checksum': str,
            'name': str,
            'zone_key': str
        }

        self.attribute_map = {
            'checksum': 'checksum',
            'name': 'name',
            'zone_key': 'zone_key'
        }

        self._checksum = checksum
        self._name = name
        self._zone_key = zone_key

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Zone':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Zone of this Zone.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def checksum(self):
        """Gets the checksum of this Zone.


        :return: The checksum of this Zone.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this Zone.


        :param checksum: The checksum of this Zone.
        :type checksum: str
        """
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")

        self._checksum = checksum

    @property
    def name(self):
        """Gets the name of this Zone.


        :return: The name of this Zone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Zone.


        :param name: The name of this Zone.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def zone_key(self):
        """Gets the zone_key of this Zone.


        :return: The zone_key of this Zone.
        :rtype: str
        """
        return self._zone_key

    @zone_key.setter
    def zone_key(self, zone_key):
        """Sets the zone_key of this Zone.


        :param zone_key: The zone_key of this Zone.
        :type zone_key: str
        """
        if zone_key is None:
            raise ValueError("Invalid value for `zone_key`, must not be `None`")

        self._zone_key = zone_key
