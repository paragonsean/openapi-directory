# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ErrorObjectSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parameter: str=None, pointer: str=None):
        """ErrorObjectSource - a model defined in OpenAPI

        :param parameter: The parameter of this ErrorObjectSource.
        :param pointer: The pointer of this ErrorObjectSource.
        """
        self.openapi_types = {
            'parameter': str,
            'pointer': str
        }

        self.attribute_map = {
            'parameter': 'parameter',
            'pointer': 'pointer'
        }

        self._parameter = parameter
        self._pointer = pointer

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorObjectSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorObject_source of this ErrorObjectSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parameter(self):
        """Gets the parameter of this ErrorObjectSource.

        If this error relates to a query parameter, the name of the parameter. 

        :return: The parameter of this ErrorObjectSource.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ErrorObjectSource.

        If this error relates to a query parameter, the name of the parameter. 

        :param parameter: The parameter of this ErrorObjectSource.
        :type parameter: str
        """

        self._parameter = parameter

    @property
    def pointer(self):
        """Gets the pointer of this ErrorObjectSource.

        If this error relates to an attribute in the request body, a rfc-6901 JSON pointer to the attribute. 

        :return: The pointer of this ErrorObjectSource.
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this ErrorObjectSource.

        If this error relates to an attribute in the request body, a rfc-6901 JSON pointer to the attribute. 

        :param pointer: The pointer of this ErrorObjectSource.
        :type pointer: str
        """

        self._pointer = pointer
