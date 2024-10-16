# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.service_allocation_view_model import ServiceAllocationViewModel
from openapi_server import util


class ServiceAllocationListViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, data: List[ServiceAllocationViewModel]=None, has_more: bool=None, object: str=None, total: int=None, url: str=None):
        """ServiceAllocationListViewModel - a model defined in OpenAPI

        :param count: The count of this ServiceAllocationListViewModel.
        :param data: The data of this ServiceAllocationListViewModel.
        :param has_more: The has_more of this ServiceAllocationListViewModel.
        :param object: The object of this ServiceAllocationListViewModel.
        :param total: The total of this ServiceAllocationListViewModel.
        :param url: The url of this ServiceAllocationListViewModel.
        """
        self.openapi_types = {
            'count': int,
            'data': List[ServiceAllocationViewModel],
            'has_more': bool,
            'object': str,
            'total': int,
            'url': str
        }

        self.attribute_map = {
            'count': 'count',
            'data': 'data',
            'has_more': 'hasMore',
            'object': 'object',
            'total': 'total',
            'url': 'url'
        }

        self._count = count
        self._data = data
        self._has_more = has_more
        self._object = object
        self._total = total
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServiceAllocationListViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServiceAllocationListViewModel of this ServiceAllocationListViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this ServiceAllocationListViewModel.


        :return: The count of this ServiceAllocationListViewModel.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ServiceAllocationListViewModel.


        :param count: The count of this ServiceAllocationListViewModel.
        :type count: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this ServiceAllocationListViewModel.


        :return: The data of this ServiceAllocationListViewModel.
        :rtype: List[ServiceAllocationViewModel]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ServiceAllocationListViewModel.


        :param data: The data of this ServiceAllocationListViewModel.
        :type data: List[ServiceAllocationViewModel]
        """

        self._data = data

    @property
    def has_more(self):
        """Gets the has_more of this ServiceAllocationListViewModel.


        :return: The has_more of this ServiceAllocationListViewModel.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this ServiceAllocationListViewModel.


        :param has_more: The has_more of this ServiceAllocationListViewModel.
        :type has_more: bool
        """

        self._has_more = has_more

    @property
    def object(self):
        """Gets the object of this ServiceAllocationListViewModel.


        :return: The object of this ServiceAllocationListViewModel.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ServiceAllocationListViewModel.


        :param object: The object of this ServiceAllocationListViewModel.
        :type object: str
        """

        self._object = object

    @property
    def total(self):
        """Gets the total of this ServiceAllocationListViewModel.


        :return: The total of this ServiceAllocationListViewModel.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ServiceAllocationListViewModel.


        :param total: The total of this ServiceAllocationListViewModel.
        :type total: int
        """

        self._total = total

    @property
    def url(self):
        """Gets the url of this ServiceAllocationListViewModel.


        :return: The url of this ServiceAllocationListViewModel.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ServiceAllocationListViewModel.


        :param url: The url of this ServiceAllocationListViewModel.
        :type url: str
        """

        self._url = url
