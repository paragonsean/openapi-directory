# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AlertErrorDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error_code: str=None, error_message: str=None, occurrences: int=None):
        """AlertErrorDetails - a model defined in OpenAPI

        :param error_code: The error_code of this AlertErrorDetails.
        :param error_message: The error_message of this AlertErrorDetails.
        :param occurrences: The occurrences of this AlertErrorDetails.
        """
        self.openapi_types = {
            'error_code': str,
            'error_message': str,
            'occurrences': int
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'occurrences': 'occurrences'
        }

        self._error_code = error_code
        self._error_message = error_message
        self._occurrences = occurrences

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlertErrorDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AlertErrorDetails of this AlertErrorDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self):
        """Gets the error_code of this AlertErrorDetails.

        Error code.

        :return: The error_code of this AlertErrorDetails.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AlertErrorDetails.

        Error code.

        :param error_code: The error_code of this AlertErrorDetails.
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this AlertErrorDetails.

        Error Message.

        :return: The error_message of this AlertErrorDetails.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this AlertErrorDetails.

        Error Message.

        :param error_message: The error_message of this AlertErrorDetails.
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def occurrences(self):
        """Gets the occurrences of this AlertErrorDetails.

        Number of occurrences.

        :return: The occurrences of this AlertErrorDetails.
        :rtype: int
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this AlertErrorDetails.

        Number of occurrences.

        :param occurrences: The occurrences of this AlertErrorDetails.
        :type occurrences: int
        """

        self._occurrences = occurrences
