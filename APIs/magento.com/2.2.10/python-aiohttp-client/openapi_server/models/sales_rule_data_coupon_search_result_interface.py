# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.framework_search_criteria_interface import FrameworkSearchCriteriaInterface
from openapi_server.models.sales_rule_data_coupon_interface import SalesRuleDataCouponInterface
from openapi_server import util


class SalesRuleDataCouponSearchResultInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[SalesRuleDataCouponInterface]=None, search_criteria: FrameworkSearchCriteriaInterface=None, total_count: int=None):
        """SalesRuleDataCouponSearchResultInterface - a model defined in OpenAPI

        :param items: The items of this SalesRuleDataCouponSearchResultInterface.
        :param search_criteria: The search_criteria of this SalesRuleDataCouponSearchResultInterface.
        :param total_count: The total_count of this SalesRuleDataCouponSearchResultInterface.
        """
        self.openapi_types = {
            'items': List[SalesRuleDataCouponInterface],
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
    def from_dict(cls, dikt: dict) -> 'SalesRuleDataCouponSearchResultInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-rule-data-coupon-search-result-interface of this SalesRuleDataCouponSearchResultInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this SalesRuleDataCouponSearchResultInterface.

        Rules.

        :return: The items of this SalesRuleDataCouponSearchResultInterface.
        :rtype: List[SalesRuleDataCouponInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SalesRuleDataCouponSearchResultInterface.

        Rules.

        :param items: The items of this SalesRuleDataCouponSearchResultInterface.
        :type items: List[SalesRuleDataCouponInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def search_criteria(self):
        """Gets the search_criteria of this SalesRuleDataCouponSearchResultInterface.


        :return: The search_criteria of this SalesRuleDataCouponSearchResultInterface.
        :rtype: FrameworkSearchCriteriaInterface
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """Sets the search_criteria of this SalesRuleDataCouponSearchResultInterface.


        :param search_criteria: The search_criteria of this SalesRuleDataCouponSearchResultInterface.
        :type search_criteria: FrameworkSearchCriteriaInterface
        """
        if search_criteria is None:
            raise ValueError("Invalid value for `search_criteria`, must not be `None`")

        self._search_criteria = search_criteria

    @property
    def total_count(self):
        """Gets the total_count of this SalesRuleDataCouponSearchResultInterface.

        Total count.

        :return: The total_count of this SalesRuleDataCouponSearchResultInterface.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SalesRuleDataCouponSearchResultInterface.

        Total count.

        :param total_count: The total_count of this SalesRuleDataCouponSearchResultInterface.
        :type total_count: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count
