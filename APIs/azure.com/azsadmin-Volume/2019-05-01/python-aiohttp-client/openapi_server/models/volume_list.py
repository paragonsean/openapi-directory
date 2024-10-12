# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.volume import Volume
from openapi_server import util


class VolumeList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[Volume]=None):
        """VolumeList - a model defined in OpenAPI

        :param next_link: The next_link of this VolumeList.
        :param value: The value of this VolumeList.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[Volume]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VolumeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VolumeList of this VolumeList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this VolumeList.

        URI to the next page.

        :return: The next_link of this VolumeList.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this VolumeList.

        URI to the next page.

        :param next_link: The next_link of this VolumeList.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this VolumeList.

        List of storage volumes.

        :return: The value of this VolumeList.
        :rtype: List[Volume]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this VolumeList.

        List of storage volumes.

        :param value: The value of this VolumeList.
        :type value: List[Volume]
        """

        self._value = value
