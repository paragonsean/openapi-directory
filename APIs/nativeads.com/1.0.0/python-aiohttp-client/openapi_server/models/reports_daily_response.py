# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.reports_daily_item import ReportsDailyItem
from openapi_server.models.totals import Totals
from openapi_server import util


class ReportsDailyResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[ReportsDailyItem]=None, success: bool=None, total_count: int=None, totals: Totals=None):
        """ReportsDailyResponse - a model defined in OpenAPI

        :param items: The items of this ReportsDailyResponse.
        :param success: The success of this ReportsDailyResponse.
        :param total_count: The total_count of this ReportsDailyResponse.
        :param totals: The totals of this ReportsDailyResponse.
        """
        self.openapi_types = {
            'items': List[ReportsDailyItem],
            'success': bool,
            'total_count': int,
            'totals': Totals
        }

        self.attribute_map = {
            'items': 'items',
            'success': 'success',
            'total_count': 'total_count',
            'totals': 'totals'
        }

        self._items = items
        self._success = success
        self._total_count = total_count
        self._totals = totals

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReportsDailyResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The reportsDailyResponse of this ReportsDailyResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this ReportsDailyResponse.


        :return: The items of this ReportsDailyResponse.
        :rtype: List[ReportsDailyItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ReportsDailyResponse.


        :param items: The items of this ReportsDailyResponse.
        :type items: List[ReportsDailyItem]
        """

        self._items = items

    @property
    def success(self):
        """Gets the success of this ReportsDailyResponse.


        :return: The success of this ReportsDailyResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ReportsDailyResponse.


        :param success: The success of this ReportsDailyResponse.
        :type success: bool
        """

        self._success = success

    @property
    def total_count(self):
        """Gets the total_count of this ReportsDailyResponse.


        :return: The total_count of this ReportsDailyResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ReportsDailyResponse.


        :param total_count: The total_count of this ReportsDailyResponse.
        :type total_count: int
        """

        self._total_count = total_count

    @property
    def totals(self):
        """Gets the totals of this ReportsDailyResponse.


        :return: The totals of this ReportsDailyResponse.
        :rtype: Totals
        """
        return self._totals

    @totals.setter
    def totals(self, totals):
        """Sets the totals of this ReportsDailyResponse.


        :param totals: The totals of this ReportsDailyResponse.
        :type totals: Totals
        """

        self._totals = totals
