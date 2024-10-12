# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.bill import Bill
from openapi_server import util


class BillList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bills: List[Bill]=None, page_number: int=None, page_size: int=None, total_count: int=None):
        """BillList - a model defined in OpenAPI

        :param bills: The bills of this BillList.
        :param page_number: The page_number of this BillList.
        :param page_size: The page_size of this BillList.
        :param total_count: The total_count of this BillList.
        """
        self.openapi_types = {
            'bills': List[Bill],
            'page_number': int,
            'page_size': int,
            'total_count': int
        }

        self.attribute_map = {
            'bills': 'Bills',
            'page_number': 'PageNumber',
            'page_size': 'PageSize',
            'total_count': 'TotalCount'
        }

        self._bills = bills
        self._page_number = page_number
        self._page_size = page_size
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BillList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BillList of this BillList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bills(self):
        """Gets the bills of this BillList.


        :return: The bills of this BillList.
        :rtype: List[Bill]
        """
        return self._bills

    @bills.setter
    def bills(self, bills):
        """Sets the bills of this BillList.


        :param bills: The bills of this BillList.
        :type bills: List[Bill]
        """

        self._bills = bills

    @property
    def page_number(self):
        """Gets the page_number of this BillList.


        :return: The page_number of this BillList.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this BillList.


        :param page_number: The page_number of this BillList.
        :type page_number: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this BillList.


        :return: The page_size of this BillList.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this BillList.


        :param page_size: The page_size of this BillList.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def total_count(self):
        """Gets the total_count of this BillList.


        :return: The total_count of this BillList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this BillList.


        :param total_count: The total_count of this BillList.
        :type total_count: int
        """

        self._total_count = total_count
