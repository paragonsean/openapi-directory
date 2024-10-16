# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Department(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: object=None, label: str=None):
        """Department - a model defined in OpenAPI

        :param value: The value of this Department.
        :param label: The label of this Department.
        """
        self.openapi_types = {
            'value': object,
            'label': str
        }

        self.attribute_map = {
            'value': 'value',
            'label': 'label'
        }

        self._value = value
        self._label = label

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Department':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Department of this Department.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this Department.


        :return: The value of this Department.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Department.


        :param value: The value of this Department.
        :type value: object
        """

        self._value = value

    @property
    def label(self):
        """Gets the label of this Department.


        :return: The label of this Department.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Department.


        :param label: The label of this Department.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label
