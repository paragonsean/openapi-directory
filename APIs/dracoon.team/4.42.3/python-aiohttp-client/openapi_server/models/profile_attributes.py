# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.key_value_entry import KeyValueEntry
from openapi_server.models.range import Range
from openapi_server import util


class ProfileAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[KeyValueEntry]=None, range: Range=None):
        """ProfileAttributes - a model defined in OpenAPI

        :param items: The items of this ProfileAttributes.
        :param range: The range of this ProfileAttributes.
        """
        self.openapi_types = {
            'items': List[KeyValueEntry],
            'range': Range
        }

        self.attribute_map = {
            'items': 'items',
            'range': 'range'
        }

        self._items = items
        self._range = range

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProfileAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProfileAttributes of this ProfileAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this ProfileAttributes.

        List of key-value pairs

        :return: The items of this ProfileAttributes.
        :rtype: List[KeyValueEntry]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ProfileAttributes.

        List of key-value pairs

        :param items: The items of this ProfileAttributes.
        :type items: List[KeyValueEntry]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def range(self):
        """Gets the range of this ProfileAttributes.


        :return: The range of this ProfileAttributes.
        :rtype: Range
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this ProfileAttributes.


        :param range: The range of this ProfileAttributes.
        :type range: Range
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")

        self._range = range
