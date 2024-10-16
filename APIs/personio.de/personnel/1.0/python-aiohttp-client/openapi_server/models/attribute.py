# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Attribute(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, label: str=None, value: object=None):
        """Attribute - a model defined in OpenAPI

        :param label: The label of this Attribute.
        :param value: The value of this Attribute.
        """
        self.openapi_types = {
            'label': str,
            'value': object
        }

        self.attribute_map = {
            'label': 'label',
            'value': 'value'
        }

        self._label = label
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Attribute':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Attribute of this Attribute.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def label(self):
        """Gets the label of this Attribute.


        :return: The label of this Attribute.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Attribute.


        :param label: The label of this Attribute.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def value(self):
        """Gets the value of this Attribute.


        :return: The value of this Attribute.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Attribute.


        :param value: The value of this Attribute.
        :type value: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
