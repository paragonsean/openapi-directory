# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WarningSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, example: str=None, parameter: str=None, pointer: str=None):
        """WarningSource - a model defined in OpenAPI

        :param example: The example of this WarningSource.
        :param parameter: The parameter of this WarningSource.
        :param pointer: The pointer of this WarningSource.
        """
        self.openapi_types = {
            'example': str,
            'parameter': str,
            'pointer': str
        }

        self.attribute_map = {
            'example': 'example',
            'parameter': 'parameter',
            'pointer': 'pointer'
        }

        self._example = example
        self._parameter = parameter
        self._pointer = pointer

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WarningSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Warning_Source of this WarningSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def example(self):
        """Gets the example of this WarningSource.

        A sample input to guide the user when resolving this issu

        :return: The example of this WarningSource.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this WarningSource.

        A sample input to guide the user when resolving this issu

        :param example: The example of this WarningSource.
        :type example: str
        """

        self._example = example

    @property
    def parameter(self):
        """Gets the parameter of this WarningSource.

        The key of the URI path or query parameter that caused the error

        :return: The parameter of this WarningSource.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this WarningSource.

        The key of the URI path or query parameter that caused the error

        :param parameter: The parameter of this WarningSource.
        :type parameter: str
        """

        self._parameter = parameter

    @property
    def pointer(self):
        """Gets the pointer of this WarningSource.

        A JSON Pointer [RFC6901] to the associated entity in the request body that caused this error

        :return: The pointer of this WarningSource.
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this WarningSource.

        A JSON Pointer [RFC6901] to the associated entity in the request body that caused this error

        :param pointer: The pointer of this WarningSource.
        :type pointer: str
        """

        self._pointer = pointer
