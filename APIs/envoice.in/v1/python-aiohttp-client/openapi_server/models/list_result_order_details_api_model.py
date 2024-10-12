# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_error_info import IErrorInfo
from openapi_server.models.order_details_api_model import OrderDetailsApiModel
from openapi_server import util


class ListResultOrderDetailsApiModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, error_messages: List[IErrorInfo]=None, is_faulted: bool=None, result: List[OrderDetailsApiModel]=None, total_count: int=None):
        """ListResultOrderDetailsApiModel - a model defined in OpenAPI

        :param count: The count of this ListResultOrderDetailsApiModel.
        :param error_messages: The error_messages of this ListResultOrderDetailsApiModel.
        :param is_faulted: The is_faulted of this ListResultOrderDetailsApiModel.
        :param result: The result of this ListResultOrderDetailsApiModel.
        :param total_count: The total_count of this ListResultOrderDetailsApiModel.
        """
        self.openapi_types = {
            'count': int,
            'error_messages': List[IErrorInfo],
            'is_faulted': bool,
            'result': List[OrderDetailsApiModel],
            'total_count': int
        }

        self.attribute_map = {
            'count': 'Count',
            'error_messages': 'ErrorMessages',
            'is_faulted': 'IsFaulted',
            'result': 'Result',
            'total_count': 'TotalCount'
        }

        self._count = count
        self._error_messages = error_messages
        self._is_faulted = is_faulted
        self._result = result
        self._total_count = total_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListResultOrderDetailsApiModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListResult_OrderDetailsApiModel_ of this ListResultOrderDetailsApiModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this ListResultOrderDetailsApiModel.


        :return: The count of this ListResultOrderDetailsApiModel.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListResultOrderDetailsApiModel.


        :param count: The count of this ListResultOrderDetailsApiModel.
        :type count: int
        """

        self._count = count

    @property
    def error_messages(self):
        """Gets the error_messages of this ListResultOrderDetailsApiModel.


        :return: The error_messages of this ListResultOrderDetailsApiModel.
        :rtype: List[IErrorInfo]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        """Sets the error_messages of this ListResultOrderDetailsApiModel.


        :param error_messages: The error_messages of this ListResultOrderDetailsApiModel.
        :type error_messages: List[IErrorInfo]
        """

        self._error_messages = error_messages

    @property
    def is_faulted(self):
        """Gets the is_faulted of this ListResultOrderDetailsApiModel.


        :return: The is_faulted of this ListResultOrderDetailsApiModel.
        :rtype: bool
        """
        return self._is_faulted

    @is_faulted.setter
    def is_faulted(self, is_faulted):
        """Sets the is_faulted of this ListResultOrderDetailsApiModel.


        :param is_faulted: The is_faulted of this ListResultOrderDetailsApiModel.
        :type is_faulted: bool
        """

        self._is_faulted = is_faulted

    @property
    def result(self):
        """Gets the result of this ListResultOrderDetailsApiModel.


        :return: The result of this ListResultOrderDetailsApiModel.
        :rtype: List[OrderDetailsApiModel]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListResultOrderDetailsApiModel.


        :param result: The result of this ListResultOrderDetailsApiModel.
        :type result: List[OrderDetailsApiModel]
        """

        self._result = result

    @property
    def total_count(self):
        """Gets the total_count of this ListResultOrderDetailsApiModel.


        :return: The total_count of this ListResultOrderDetailsApiModel.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListResultOrderDetailsApiModel.


        :param total_count: The total_count of this ListResultOrderDetailsApiModel.
        :type total_count: int
        """

        self._total_count = total_count
