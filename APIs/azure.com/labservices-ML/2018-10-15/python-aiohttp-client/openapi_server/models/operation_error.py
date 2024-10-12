# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OperationError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):
        """OperationError - a model defined in OpenAPI

        :param code: The code of this OperationError.
        :param message: The message of this OperationError.
        """
        self.openapi_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OperationError':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OperationError of this OperationError.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this OperationError.

        The error code of the operation error.

        :return: The code of this OperationError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OperationError.

        The error code of the operation error.

        :param code: The code of this OperationError.
        :type code: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this OperationError.

        The error message of the operation error.

        :return: The message of this OperationError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OperationError.

        The error message of the operation error.

        :param message: The message of this OperationError.
        :type message: str
        """

        self._message = message
