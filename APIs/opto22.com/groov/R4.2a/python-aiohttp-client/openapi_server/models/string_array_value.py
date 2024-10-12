# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tag_value import TagValue
from openapi_server import util


class StringArrayValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value_type: str=None, value: List[str]=None):
        """StringArrayValue - a model defined in OpenAPI

        :param value_type: The value_type of this StringArrayValue.
        :param value: The value of this StringArrayValue.
        """
        self.openapi_types = {
            'value_type': str,
            'value': List[str]
        }

        self.attribute_map = {
            'value_type': 'valueType',
            'value': 'value'
        }

        self._value_type = value_type
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StringArrayValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The stringArrayValue of this StringArrayValue.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value_type(self):
        """Gets the value_type of this StringArrayValue.


        :return: The value_type of this StringArrayValue.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this StringArrayValue.


        :param value_type: The value_type of this StringArrayValue.
        :type value_type: str
        """
        if value_type is None:
            raise ValueError("Invalid value for `value_type`, must not be `None`")

        self._value_type = value_type

    @property
    def value(self):
        """Gets the value of this StringArrayValue.


        :return: The value of this StringArrayValue.
        :rtype: List[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StringArrayValue.


        :param value: The value of this StringArrayValue.
        :type value: List[str]
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
