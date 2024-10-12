# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Response11(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error: str=None, error_description: str=None):
        """Response11 - a model defined in OpenAPI

        :param error: The error of this Response11.
        :param error_description: The error_description of this Response11.
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
    def from_dict(cls, dikt: dict) -> 'Response11':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Response11 of this Response11.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this Response11.

        auth_failure

        :return: The error of this Response11.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Response11.

        auth_failure

        :param error: The error of this Response11.
        :type error: str
        """

        self._error = error

    @property
    def error_description(self):
        """Gets the error_description of this Response11.

        The data on Aadhaar does not match with one or more of Aadhaar, Name, DOB and Gender data provided. Aadhaar demographic authentication failure.

        :return: The error_description of this Response11.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this Response11.

        The data on Aadhaar does not match with one or more of Aadhaar, Name, DOB and Gender data provided. Aadhaar demographic authentication failure.

        :param error_description: The error_description of this Response11.
        :type error_description: str
        """

        self._error_description = error_description
