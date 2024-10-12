# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InHeader(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, remove: str=None, type: str=None):
        """InHeader - a model defined in OpenAPI

        :param name: The name of this InHeader.
        :param remove: The remove of this InHeader.
        :param type: The type of this InHeader.
        """
        self.openapi_types = {
            'name': str,
            'remove': str,
            'type': str
        }

        self.attribute_map = {
            'name': 'name',
            'remove': 'remove',
            'type': 'type'
        }

        self._name = name
        self._remove = remove
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InHeader':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InHeader of this InHeader.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this InHeader.

        Name of the header

        :return: The name of this InHeader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InHeader.

        Name of the header

        :param name: The name of this InHeader.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def remove(self):
        """Gets the remove of this InHeader.

        Remove regex inside the value, like 'Bearer '

        :return: The remove of this InHeader.
        :rtype: str
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """Sets the remove of this InHeader.

        Remove regex inside the value, like 'Bearer '

        :param remove: The remove of this InHeader.
        :type remove: str
        """
        if remove is None:
            raise ValueError("Invalid value for `remove`, must not be `None`")

        self._remove = remove

    @property
    def type(self):
        """Gets the type of this InHeader.

        String with value InHeader

        :return: The type of this InHeader.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InHeader.

        String with value InHeader

        :param type: The type of this InHeader.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
