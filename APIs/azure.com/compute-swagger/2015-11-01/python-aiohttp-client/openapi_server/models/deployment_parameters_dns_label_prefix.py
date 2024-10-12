# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DeploymentParametersDnsLabelPrefix(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: str=None):
        """DeploymentParametersDnsLabelPrefix - a model defined in OpenAPI

        :param value: The value of this DeploymentParametersDnsLabelPrefix.
        """
        self.openapi_types = {
            'value': str
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeploymentParametersDnsLabelPrefix':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeploymentParameters_dnsLabelPrefix of this DeploymentParametersDnsLabelPrefix.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this DeploymentParametersDnsLabelPrefix.

        Unique DNS Name for the Public IP used to access the Virtual Machine.

        :return: The value of this DeploymentParametersDnsLabelPrefix.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DeploymentParametersDnsLabelPrefix.

        Unique DNS Name for the Public IP used to access the Virtual Machine.

        :param value: The value of this DeploymentParametersDnsLabelPrefix.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
