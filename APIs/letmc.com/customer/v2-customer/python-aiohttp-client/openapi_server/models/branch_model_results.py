# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.branch_model import BranchModel
from openapi_server import util


class BranchModelResults(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, data: List[BranchModel]=None):
        """BranchModelResults - a model defined in OpenAPI

        :param count: The count of this BranchModelResults.
        :param data: The data of this BranchModelResults.
        """
        self.openapi_types = {
            'count': int,
            'data': List[BranchModel]
        }

        self.attribute_map = {
            'count': 'Count',
            'data': 'Data'
        }

        self._count = count
        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BranchModelResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BranchModelResults of this BranchModelResults.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this BranchModelResults.

        The total number of results available for all pages

        :return: The count of this BranchModelResults.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BranchModelResults.

        The total number of results available for all pages

        :param count: The count of this BranchModelResults.
        :type count: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this BranchModelResults.

        The resulting data returned from the paged query range

        :return: The data of this BranchModelResults.
        :rtype: List[BranchModel]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BranchModelResults.

        The resulting data returned from the paged query range

        :param data: The data of this BranchModelResults.
        :type data: List[BranchModel]
        """

        self._data = data
