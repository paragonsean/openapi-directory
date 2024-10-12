# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.operation_error import OperationError
from openapi_server import util


class OperationResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error: OperationError=None, status: str=None):
        """OperationResult - a model defined in OpenAPI

        :param error: The error of this OperationResult.
        :param status: The status of this OperationResult.
        """
        self.openapi_types = {
            'error': OperationError,
            'status': str
        }

        self.attribute_map = {
            'error': 'error',
            'status': 'status'
        }

        self._error = error
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OperationResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OperationResult of this OperationResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this OperationResult.


        :return: The error of this OperationResult.
        :rtype: OperationError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OperationResult.


        :param error: The error of this OperationResult.
        :type error: OperationError
        """

        self._error = error

    @property
    def status(self):
        """Gets the status of this OperationResult.

        The operation status.

        :return: The status of this OperationResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OperationResult.

        The operation status.

        :param status: The status of this OperationResult.
        :type status: str
        """

        self._status = status
