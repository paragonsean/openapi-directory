# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CustomVitalValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: str=None, vital_type: int=None):
        """CustomVitalValue - a model defined in OpenAPI

        :param value: The value of this CustomVitalValue.
        :param vital_type: The vital_type of this CustomVitalValue.
        """
        self.openapi_types = {
            'value': str,
            'vital_type': int
        }

        self.attribute_map = {
            'value': 'value',
            'vital_type': 'vital_type'
        }

        self._value = value
        self._vital_type = vital_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CustomVitalValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CustomVitalValue of this CustomVitalValue.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this CustomVitalValue.

        

        :return: The value of this CustomVitalValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomVitalValue.

        

        :param value: The value of this CustomVitalValue.
        :type value: str
        """

        self._value = value

    @property
    def vital_type(self):
        """Gets the vital_type of this CustomVitalValue.

        

        :return: The vital_type of this CustomVitalValue.
        :rtype: int
        """
        return self._vital_type

    @vital_type.setter
    def vital_type(self, vital_type):
        """Sets the vital_type of this CustomVitalValue.

        

        :param vital_type: The vital_type of this CustomVitalValue.
        :type vital_type: int
        """

        self._vital_type = vital_type
