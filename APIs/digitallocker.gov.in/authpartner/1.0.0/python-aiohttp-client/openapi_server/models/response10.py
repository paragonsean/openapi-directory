# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Response10(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error: str=None, error_description: str=None):
        """Response10 - a model defined in OpenAPI

        :param error: The error of this Response10.
        :param error_description: The error_description of this Response10.
        """
        self.openapi_types = {
            'error': str,
            'error_description': str
        }

        self.attribute_map = {
            'error': 'error',
            'error_description': 'error_description'
        }

        self._error = error
        self._error_description = error_description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Response10':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Response10 of this Response10.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this Response10.

        mobile_exists

        :return: The error of this Response10.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Response10.

        mobile_exists

        :param error: The error of this Response10.
        :type error: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this Response10.

        A DigiLocker account already exists with this mobile number.

        :return: The error_description of this Response10.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this Response10.

        A DigiLocker account already exists with this mobile number.

        :param error_description: The error_description of this Response10.
        :type error_description: str
        """

        self._error_description = error_description
