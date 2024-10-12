# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.framework_search_criteria_interface import FrameworkSearchCriteriaInterface
from openapi_server.models.sales_data_creditmemo_comment_interface import SalesDataCreditmemoCommentInterface
from openapi_server import util


class SalesDataCreditmemoCommentSearchResultInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[SalesDataCreditmemoCommentInterface]=None, search_criteria: FrameworkSearchCriteriaInterface=None, total_count: int=None):
        """SalesDataCreditmemoCommentSearchResultInterface - a model defined in OpenAPI

        :param items: The items of this SalesDataCreditmemoCommentSearchResultInterface.
        :param search_criteria: The search_criteria of this SalesDataCreditmemoCommentSearchResultInterface.
        :param total_count: The total_count of this SalesDataCreditmemoCommentSearchResultInterface.
        """
        self.openapi_types = {
            'items': List[SalesDataCreditmemoCommentInterface],
            'search_criteria': FrameworkSearchCriteriaInterface,
            'total_count': int
        }

        self.attribute_map = {
            'items': 'items',
            'search_criteria': 'search_criteria',
            'total_count': 'total_count'
        }

        self._items = items
        self._search_criteria = search_criteria
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataCreditmemoCommentSearchResultInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-creditmemo-comment-search-result-interface of this SalesDataCreditmemoCommentSearchResultInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this SalesDataCreditmemoCommentSearchResultInterface.

        Array of collection items.

        :return: The items of this SalesDataCreditmemoCommentSearchResultInterface.
        :rtype: List[SalesDataCreditmemoCommentInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SalesDataCreditmemoCommentSearchResultInterface.

        Array of collection items.

        :param items: The items of this SalesDataCreditmemoCommentSearchResultInterface.
        :type items: List[SalesDataCreditmemoCommentInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def search_criteria(self):
        """Gets the search_criteria of this SalesDataCreditmemoCommentSearchResultInterface.


        :return: The search_criteria of this SalesDataCreditmemoCommentSearchResultInterface.
        :rtype: FrameworkSearchCriteriaInterface
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """Sets the search_criteria of this SalesDataCreditmemoCommentSearchResultInterface.


        :param search_criteria: The search_criteria of this SalesDataCreditmemoCommentSearchResultInterface.
        :type search_criteria: FrameworkSearchCriteriaInterface
        """
        if search_criteria is None:
            raise ValueError("Invalid value for `search_criteria`, must not be `None`")

        self._search_criteria = search_criteria

    @property
    def total_count(self):
        """Gets the total_count of this SalesDataCreditmemoCommentSearchResultInterface.

        Total count.

        :return: The total_count of this SalesDataCreditmemoCommentSearchResultInterface.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SalesDataCreditmemoCommentSearchResultInterface.

        Total count.

        :param total_count: The total_count of this SalesDataCreditmemoCommentSearchResultInterface.
        :type total_count: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count
