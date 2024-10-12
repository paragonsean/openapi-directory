# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateTagModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, color: str=None, name: str=None):
        """CreateTagModel - a model defined in OpenAPI

        :param color: The color of this CreateTagModel.
        :param name: The name of this CreateTagModel.
        """
        self.openapi_types = {
            'color': str,
            'name': str
        }

        self.attribute_map = {
            'color': 'color',
            'name': 'name'
        }

        self._color = color
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateTagModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateTagModel of this CreateTagModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color(self):
        """Gets the color of this CreateTagModel.


        :return: The color of this CreateTagModel.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CreateTagModel.


        :param color: The color of this CreateTagModel.
        :type color: str
        """
        if color is not None and len(color) > 255:
            raise ValueError("Invalid value for `color`, length must be less than or equal to `255`")
        if color is not None and len(color) < 0:
            raise ValueError("Invalid value for `color`, length must be greater than or equal to `0`")

        self._color = color

    @property
    def name(self):
        """Gets the name of this CreateTagModel.


        :return: The name of this CreateTagModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTagModel.


        :param name: The name of this CreateTagModel.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name
