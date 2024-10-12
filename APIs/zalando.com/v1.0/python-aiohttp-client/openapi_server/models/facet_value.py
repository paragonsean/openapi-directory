# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FacetValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, display_name: str=None, key: str=None):
        """FacetValue - a model defined in OpenAPI

        :param count: The count of this FacetValue.
        :param display_name: The display_name of this FacetValue.
        :param key: The key of this FacetValue.
        """
        self.openapi_types = {
            'count': int,
            'display_name': str,
            'key': str
        }

        self.attribute_map = {
            'count': 'count',
            'display_name': 'displayName',
            'key': 'key'
        }

        self._count = count
        self._display_name = display_name
        self._key = key

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FacetValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Facet-Value of this FacetValue.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this FacetValue.

        number of articles matching this filter value

        :return: The count of this FacetValue.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this FacetValue.

        number of articles matching this filter value

        :param count: The count of this FacetValue.
        :type count: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")

        self._count = count

    @property
    def display_name(self):
        """Gets the display_name of this FacetValue.


        :return: The display_name of this FacetValue.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FacetValue.


        :param display_name: The display_name of this FacetValue.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name

    @property
    def key(self):
        """Gets the key of this FacetValue.


        :return: The key of this FacetValue.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FacetValue.


        :param key: The key of this FacetValue.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key
