# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WarningsSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, example: str=None, parameter: str=None, pointer: str=None):
        """WarningsSource - a model defined in OpenAPI

        :param example: The example of this WarningsSource.
        :param parameter: The parameter of this WarningsSource.
        :param pointer: The pointer of this WarningsSource.
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
    def from_dict(cls, dikt: dict) -> 'WarningsSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The warnings_source of this WarningsSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def example(self):
        """Gets the example of this WarningsSource.

        A sample input to guide the user when resolving this issue

        :return: The example of this WarningsSource.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this WarningsSource.

        A sample input to guide the user when resolving this issue

        :param example: The example of this WarningsSource.
        :type example: str
        """

        self._example = example

    @property
    def parameter(self):
        """Gets the parameter of this WarningsSource.

        The key of the URI path or query parameter that caused the warning

        :return: The parameter of this WarningsSource.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this WarningsSource.

        The key of the URI path or query parameter that caused the warning

        :param parameter: The parameter of this WarningsSource.
        :type parameter: str
        """

        self._parameter = parameter

    @property
    def pointer(self):
        """Gets the pointer of this WarningsSource.

        A JSON Pointer RFC6901 to the associated entity in the request body that caused this warning

        :return: The pointer of this WarningsSource.
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this WarningsSource.

        A JSON Pointer RFC6901 to the associated entity in the request body that caused this warning

        :param pointer: The pointer of this WarningsSource.
        :type pointer: str
        """

        self._pointer = pointer
