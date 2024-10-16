# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.service_block_view_model import ServiceBlockViewModel
from openapi_server import util


class ServiceBlockListViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, data: List[ServiceBlockViewModel]=None, has_more: bool=None, object: str=None, total: int=None, url: str=None):
        """ServiceBlockListViewModel - a model defined in OpenAPI

        :param count: The count of this ServiceBlockListViewModel.
        :param data: The data of this ServiceBlockListViewModel.
        :param has_more: The has_more of this ServiceBlockListViewModel.
        :param object: The object of this ServiceBlockListViewModel.
        :param total: The total of this ServiceBlockListViewModel.
        :param url: The url of this ServiceBlockListViewModel.
        """
        self.openapi_types = {
            'count': int,
            'data': List[ServiceBlockViewModel],
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
    def from_dict(cls, dikt: dict) -> 'ServiceBlockListViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServiceBlockListViewModel of this ServiceBlockListViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this ServiceBlockListViewModel.


        :return: The count of this ServiceBlockListViewModel.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ServiceBlockListViewModel.


        :param count: The count of this ServiceBlockListViewModel.
        :type count: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this ServiceBlockListViewModel.


        :return: The data of this ServiceBlockListViewModel.
        :rtype: List[ServiceBlockViewModel]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ServiceBlockListViewModel.


        :param data: The data of this ServiceBlockListViewModel.
        :type data: List[ServiceBlockViewModel]
        """

        self._data = data

    @property
    def has_more(self):
        """Gets the has_more of this ServiceBlockListViewModel.


        :return: The has_more of this ServiceBlockListViewModel.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this ServiceBlockListViewModel.


        :param has_more: The has_more of this ServiceBlockListViewModel.
        :type has_more: bool
        """

        self._has_more = has_more

    @property
    def object(self):
        """Gets the object of this ServiceBlockListViewModel.


        :return: The object of this ServiceBlockListViewModel.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ServiceBlockListViewModel.


        :param object: The object of this ServiceBlockListViewModel.
        :type object: str
        """

        self._object = object

    @property
    def total(self):
        """Gets the total of this ServiceBlockListViewModel.


        :return: The total of this ServiceBlockListViewModel.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ServiceBlockListViewModel.


        :param total: The total of this ServiceBlockListViewModel.
        :type total: int
        """

        self._total = total

    @property
    def url(self):
        """Gets the url of this ServiceBlockListViewModel.


        :return: The url of this ServiceBlockListViewModel.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ServiceBlockListViewModel.


        :param url: The url of this ServiceBlockListViewModel.
        :type url: str
        """

        self._url = url
