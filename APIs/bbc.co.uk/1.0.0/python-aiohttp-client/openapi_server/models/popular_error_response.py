# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.popular_error import PopularError
from openapi_server import util


class PopularErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _schema: str=None, errors: List[PopularError]=None):
        """PopularErrorResponse - a model defined in OpenAPI

        :param _schema: The _schema of this PopularErrorResponse.
        :param errors: The errors of this PopularErrorResponse.
        """
        self.openapi_types = {
            '_schema': str,
            'errors': List[PopularError]
        }

        self.attribute_map = {
            '_schema': '$schema',
            'errors': 'errors'
        }

        self.__schema = _schema
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PopularErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PopularErrorResponse of this PopularErrorResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _schema(self):
        """Gets the _schema of this PopularErrorResponse.


        :return: The _schema of this PopularErrorResponse.
        :rtype: str
        """
        return self.__schema

    @_schema.setter
    def _schema(self, _schema):
        """Sets the _schema of this PopularErrorResponse.


        :param _schema: The _schema of this PopularErrorResponse.
        :type _schema: str
        """
        if _schema is None:
            raise ValueError("Invalid value for `_schema`, must not be `None`")

        self.__schema = _schema

    @property
    def errors(self):
        """Gets the errors of this PopularErrorResponse.


        :return: The errors of this PopularErrorResponse.
        :rtype: List[PopularError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this PopularErrorResponse.


        :param errors: The errors of this PopularErrorResponse.
        :type errors: List[PopularError]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")

        self._errors = errors
