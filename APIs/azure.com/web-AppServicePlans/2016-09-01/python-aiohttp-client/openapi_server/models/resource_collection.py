# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ResourceCollection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[str]=None):
        """ResourceCollection - a model defined in OpenAPI

        :param next_link: The next_link of this ResourceCollection.
        :param value: The value of this ResourceCollection.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[str]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourceCollection':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceCollection of this ResourceCollection.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this ResourceCollection.

        Link to next page of resources.

        :return: The next_link of this ResourceCollection.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ResourceCollection.

        Link to next page of resources.

        :param next_link: The next_link of this ResourceCollection.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this ResourceCollection.

        Collection of resources.

        :return: The value of this ResourceCollection.
        :rtype: List[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResourceCollection.

        Collection of resources.

        :param value: The value of this ResourceCollection.
        :type value: List[str]
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
