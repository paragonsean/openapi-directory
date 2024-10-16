# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SortOptionResponseSortOptionsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order: int=None, sort_name: str=None, strategy: str=None):
        """SortOptionResponseSortOptionsInner - a model defined in OpenAPI

        :param order: The order of this SortOptionResponseSortOptionsInner.
        :param sort_name: The sort_name of this SortOptionResponseSortOptionsInner.
        :param strategy: The strategy of this SortOptionResponseSortOptionsInner.
        """
        self.openapi_types = {
            'order': int,
            'sort_name': str,
            'strategy': str
        }

        self.attribute_map = {
            'order': 'order',
            'sort_name': 'sortName',
            'strategy': 'strategy'
        }

        self._order = order
        self._sort_name = sort_name
        self._strategy = strategy

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SortOptionResponseSortOptionsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SortOptionResponse_sortOptions_inner of this SortOptionResponseSortOptionsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order(self):
        """Gets the order of this SortOptionResponseSortOptionsInner.


        :return: The order of this SortOptionResponseSortOptionsInner.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this SortOptionResponseSortOptionsInner.


        :param order: The order of this SortOptionResponseSortOptionsInner.
        :type order: int
        """

        self._order = order

    @property
    def sort_name(self):
        """Gets the sort_name of this SortOptionResponseSortOptionsInner.


        :return: The sort_name of this SortOptionResponseSortOptionsInner.
        :rtype: str
        """
        return self._sort_name

    @sort_name.setter
    def sort_name(self, sort_name):
        """Sets the sort_name of this SortOptionResponseSortOptionsInner.


        :param sort_name: The sort_name of this SortOptionResponseSortOptionsInner.
        :type sort_name: str
        """

        self._sort_name = sort_name

    @property
    def strategy(self):
        """Gets the strategy of this SortOptionResponseSortOptionsInner.


        :return: The strategy of this SortOptionResponseSortOptionsInner.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this SortOptionResponseSortOptionsInner.


        :param strategy: The strategy of this SortOptionResponseSortOptionsInner.
        :type strategy: str
        """

        self._strategy = strategy
