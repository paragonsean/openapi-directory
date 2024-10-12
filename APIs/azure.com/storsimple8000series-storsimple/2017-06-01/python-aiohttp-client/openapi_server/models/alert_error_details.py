# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AlertErrorDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error_code: str=None, error_message: str=None, occurences: int=None):
        """AlertErrorDetails - a model defined in OpenAPI

        :param error_code: The error_code of this AlertErrorDetails.
        :param error_message: The error_message of this AlertErrorDetails.
        :param occurences: The occurences of this AlertErrorDetails.
        """
        self.openapi_types = {
            'error_code': str,
            'error_message': str,
            'occurences': int
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'occurences': 'occurences'
        }

        self._error_code = error_code
        self._error_message = error_message
        self._occurences = occurences

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

        The error code

        :return: The error_code of this AlertErrorDetails.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AlertErrorDetails.

        The error code

        :param error_code: The error_code of this AlertErrorDetails.
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this AlertErrorDetails.

        The error message

        :return: The error_message of this AlertErrorDetails.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this AlertErrorDetails.

        The error message

        :param error_message: The error_message of this AlertErrorDetails.
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def occurences(self):
        """Gets the occurences of this AlertErrorDetails.

        The number of occurrences

        :return: The occurences of this AlertErrorDetails.
        :rtype: int
        """
        return self._occurences

    @occurences.setter
    def occurences(self, occurences):
        """Sets the occurences of this AlertErrorDetails.

        The number of occurrences

        :param occurences: The occurences of this AlertErrorDetails.
        :type occurences: int
        """

        self._occurences = occurences
