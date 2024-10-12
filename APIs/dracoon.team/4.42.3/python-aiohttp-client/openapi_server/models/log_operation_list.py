# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.log_operation import LogOperation
from openapi_server import util


class LogOperationList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operation_list: List[LogOperation]=None):
        """LogOperationList - a model defined in OpenAPI

        :param operation_list: The operation_list of this LogOperationList.
        """
        self.openapi_types = {
            'operation_list': List[LogOperation]
        }

        self.attribute_map = {
            'operation_list': 'operationList'
        }

        self._operation_list = operation_list

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LogOperationList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LogOperationList of this LogOperationList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operation_list(self):
        """Gets the operation_list of this LogOperationList.

        List of all log operations

        :return: The operation_list of this LogOperationList.
        :rtype: List[LogOperation]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        """Sets the operation_list of this LogOperationList.

        List of all log operations

        :param operation_list: The operation_list of this LogOperationList.
        :type operation_list: List[LogOperation]
        """
        if operation_list is None:
            raise ValueError("Invalid value for `operation_list`, must not be `None`")

        self._operation_list = operation_list
