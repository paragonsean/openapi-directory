# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.o_data_query_context import ODataQueryContext
from openapi_server import util


class InlineCountQueryOption(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, context: ODataQueryContext=None, raw_value: str=None, value: int=None):
        """InlineCountQueryOption - a model defined in OpenAPI

        :param context: The context of this InlineCountQueryOption.
        :param raw_value: The raw_value of this InlineCountQueryOption.
        :param value: The value of this InlineCountQueryOption.
        """
        self.openapi_types = {
            'context': ODataQueryContext,
            'raw_value': str,
            'value': int
        }

        self.attribute_map = {
            'context': 'Context',
            'raw_value': 'RawValue',
            'value': 'Value'
        }

        self._context = context
        self._raw_value = raw_value
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineCountQueryOption':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InlineCountQueryOption of this InlineCountQueryOption.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self):
        """Gets the context of this InlineCountQueryOption.


        :return: The context of this InlineCountQueryOption.
        :rtype: ODataQueryContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this InlineCountQueryOption.


        :param context: The context of this InlineCountQueryOption.
        :type context: ODataQueryContext
        """

        self._context = context

    @property
    def raw_value(self):
        """Gets the raw_value of this InlineCountQueryOption.


        :return: The raw_value of this InlineCountQueryOption.
        :rtype: str
        """
        return self._raw_value

    @raw_value.setter
    def raw_value(self, raw_value):
        """Sets the raw_value of this InlineCountQueryOption.


        :param raw_value: The raw_value of this InlineCountQueryOption.
        :type raw_value: str
        """

        self._raw_value = raw_value

    @property
    def value(self):
        """Gets the value of this InlineCountQueryOption.


        :return: The value of this InlineCountQueryOption.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineCountQueryOption.


        :param value: The value of this InlineCountQueryOption.
        :type value: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if value not in allowed_values:
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"
                .format(value, allowed_values)
            )

        self._value = value
