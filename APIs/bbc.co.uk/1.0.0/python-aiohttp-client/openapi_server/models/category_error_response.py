# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.category_error import CategoryError
from openapi_server import util


class CategoryErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _schema: str=None, errors: List[CategoryError]=None):
        """CategoryErrorResponse - a model defined in OpenAPI

        :param _schema: The _schema of this CategoryErrorResponse.
        :param errors: The errors of this CategoryErrorResponse.
        """
        self.openapi_types = {
            '_schema': str,
            'errors': List[CategoryError]
        }

        self.attribute_map = {
            '_schema': '$schema',
            'errors': 'errors'
        }

        self.__schema = _schema
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CategoryErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CategoryErrorResponse of this CategoryErrorResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _schema(self):
        """Gets the _schema of this CategoryErrorResponse.


        :return: The _schema of this CategoryErrorResponse.
        :rtype: str
        """
        return self.__schema

    @_schema.setter
    def _schema(self, _schema):
        """Sets the _schema of this CategoryErrorResponse.


        :param _schema: The _schema of this CategoryErrorResponse.
        :type _schema: str
        """
        if _schema is None:
            raise ValueError("Invalid value for `_schema`, must not be `None`")

        self.__schema = _schema

    @property
    def errors(self):
        """Gets the errors of this CategoryErrorResponse.


        :return: The errors of this CategoryErrorResponse.
        :rtype: List[CategoryError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CategoryErrorResponse.


        :param errors: The errors of this CategoryErrorResponse.
        :type errors: List[CategoryError]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")

        self._errors = errors
