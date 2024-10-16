# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildsGetLog200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: List[str]=None):
        """BuildsGetLog200Response - a model defined in OpenAPI

        :param value: The value of this BuildsGetLog200Response.
        """
        self.openapi_types = {
            'value': List[str]
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildsGetLog200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The builds_getLog_200_response of this BuildsGetLog200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this BuildsGetLog200Response.


        :return: The value of this BuildsGetLog200Response.
        :rtype: List[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BuildsGetLog200Response.


        :param value: The value of this BuildsGetLog200Response.
        :type value: List[str]
        """

        self._value = value
