# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.variable_create_or_update_properties import VariableCreateOrUpdateProperties
from openapi_server import util


class VariableCreateOrUpdateParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, properties: VariableCreateOrUpdateProperties=None):
        """VariableCreateOrUpdateParameters - a model defined in OpenAPI

        :param name: The name of this VariableCreateOrUpdateParameters.
        :param properties: The properties of this VariableCreateOrUpdateParameters.
        """
        self.openapi_types = {
            'name': str,
            'properties': VariableCreateOrUpdateProperties
        }

        self.attribute_map = {
            'name': 'name',
            'properties': 'properties'
        }

        self._name = name
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VariableCreateOrUpdateParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VariableCreateOrUpdateParameters of this VariableCreateOrUpdateParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this VariableCreateOrUpdateParameters.

        Gets or sets the name of the variable.

        :return: The name of this VariableCreateOrUpdateParameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableCreateOrUpdateParameters.

        Gets or sets the name of the variable.

        :param name: The name of this VariableCreateOrUpdateParameters.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this VariableCreateOrUpdateParameters.


        :return: The properties of this VariableCreateOrUpdateParameters.
        :rtype: VariableCreateOrUpdateProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this VariableCreateOrUpdateParameters.


        :param properties: The properties of this VariableCreateOrUpdateParameters.
        :type properties: VariableCreateOrUpdateProperties
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties
