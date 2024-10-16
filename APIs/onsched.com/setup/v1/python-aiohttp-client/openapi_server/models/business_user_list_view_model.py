# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.business_user_view_model import BusinessUserViewModel
from openapi_server import util


class BusinessUserListViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, data: List[BusinessUserViewModel]=None, has_more: bool=None, object: str=None, total: int=None, url: str=None):
        """BusinessUserListViewModel - a model defined in OpenAPI

        :param count: The count of this BusinessUserListViewModel.
        :param data: The data of this BusinessUserListViewModel.
        :param has_more: The has_more of this BusinessUserListViewModel.
        :param object: The object of this BusinessUserListViewModel.
        :param total: The total of this BusinessUserListViewModel.
        :param url: The url of this BusinessUserListViewModel.
        """
        self.openapi_types = {
            'count': int,
            'data': List[BusinessUserViewModel],
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
    def from_dict(cls, dikt: dict) -> 'BusinessUserListViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BusinessUserListViewModel of this BusinessUserListViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this BusinessUserListViewModel.


        :return: The count of this BusinessUserListViewModel.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BusinessUserListViewModel.


        :param count: The count of this BusinessUserListViewModel.
        :type count: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this BusinessUserListViewModel.


        :return: The data of this BusinessUserListViewModel.
        :rtype: List[BusinessUserViewModel]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BusinessUserListViewModel.


        :param data: The data of this BusinessUserListViewModel.
        :type data: List[BusinessUserViewModel]
        """

        self._data = data

    @property
    def has_more(self):
        """Gets the has_more of this BusinessUserListViewModel.


        :return: The has_more of this BusinessUserListViewModel.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this BusinessUserListViewModel.


        :param has_more: The has_more of this BusinessUserListViewModel.
        :type has_more: bool
        """

        self._has_more = has_more

    @property
    def object(self):
        """Gets the object of this BusinessUserListViewModel.


        :return: The object of this BusinessUserListViewModel.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this BusinessUserListViewModel.


        :param object: The object of this BusinessUserListViewModel.
        :type object: str
        """

        self._object = object

    @property
    def total(self):
        """Gets the total of this BusinessUserListViewModel.


        :return: The total of this BusinessUserListViewModel.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BusinessUserListViewModel.


        :param total: The total of this BusinessUserListViewModel.
        :type total: int
        """

        self._total = total

    @property
    def url(self):
        """Gets the url of this BusinessUserListViewModel.


        :return: The url of this BusinessUserListViewModel.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BusinessUserListViewModel.


        :param url: The url of this BusinessUserListViewModel.
        :type url: str
        """

        self._url = url
