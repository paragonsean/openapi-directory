# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.text_broadcast import TextBroadcast
from openapi_server import util


class TextBroadcastPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[TextBroadcast]=None, limit: int=None, offset: int=None, total_count: int=None):
        """TextBroadcastPage - a model defined in OpenAPI

        :param items: The items of this TextBroadcastPage.
        :param limit: The limit of this TextBroadcastPage.
        :param offset: The offset of this TextBroadcastPage.
        :param total_count: The total_count of this TextBroadcastPage.
        """
        self.openapi_types = {
            'items': List[TextBroadcast],
            'limit': int,
            'offset': int,
            'total_count': int
        }

        self.attribute_map = {
            'items': 'items',
            'limit': 'limit',
            'offset': 'offset',
            'total_count': 'totalCount'
        }

        self._items = items
        self._limit = limit
        self._offset = offset
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TextBroadcastPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TextBroadcastPage of this TextBroadcastPage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this TextBroadcastPage.


        :return: The items of this TextBroadcastPage.
        :rtype: List[TextBroadcast]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TextBroadcastPage.


        :param items: The items of this TextBroadcastPage.
        :type items: List[TextBroadcast]
        """

        self._items = items

    @property
    def limit(self):
        """Gets the limit of this TextBroadcastPage.

        A maximum number of returned items. If items.size() < limit assume no more items

        :return: The limit of this TextBroadcastPage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TextBroadcastPage.

        A maximum number of returned items. If items.size() < limit assume no more items

        :param limit: The limit of this TextBroadcastPage.
        :type limit: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this TextBroadcastPage.

        An offset from a start of paging source

        :return: The offset of this TextBroadcastPage.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TextBroadcastPage.

        An offset from a start of paging source

        :param offset: The offset of this TextBroadcastPage.
        :type offset: int
        """

        self._offset = offset

    @property
    def total_count(self):
        """Gets the total_count of this TextBroadcastPage.

        Total count of available results. -1 if unknown

        :return: The total_count of this TextBroadcastPage.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this TextBroadcastPage.

        Total count of available results. -1 if unknown

        :param total_count: The total_count of this TextBroadcastPage.
        :type total_count: int
        """

        self._total_count = total_count
