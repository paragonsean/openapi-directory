# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TimeOffTypeResourceAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """TimeOffTypeResourceAttributes - a model defined in OpenAPI

        :param name: The name of this TimeOffTypeResourceAttributes.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TimeOffTypeResourceAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TimeOffTypeResource_attributes of this TimeOffTypeResourceAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TimeOffTypeResourceAttributes.


        :return: The name of this TimeOffTypeResourceAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimeOffTypeResourceAttributes.


        :param name: The name of this TimeOffTypeResourceAttributes.
        :type name: str
        """

        self._name = name
