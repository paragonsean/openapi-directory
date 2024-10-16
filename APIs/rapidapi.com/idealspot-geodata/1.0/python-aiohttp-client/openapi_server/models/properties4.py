# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Properties4(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """Properties4 - a model defined in OpenAPI

        :param name: The name of this Properties4.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Properties4':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Properties4 of this Properties4.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Properties4.


        :return: The name of this Properties4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Properties4.


        :param name: The name of this Properties4.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
