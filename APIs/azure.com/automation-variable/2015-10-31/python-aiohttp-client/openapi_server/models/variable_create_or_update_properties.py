# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VariableCreateOrUpdateProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, is_encrypted: bool=None, value: str=None):
        """VariableCreateOrUpdateProperties - a model defined in OpenAPI

        :param description: The description of this VariableCreateOrUpdateProperties.
        :param is_encrypted: The is_encrypted of this VariableCreateOrUpdateProperties.
        :param value: The value of this VariableCreateOrUpdateProperties.
        """
        self.openapi_types = {
            'description': str,
            'is_encrypted': bool,
            'value': str
        }

        self.attribute_map = {
            'description': 'description',
            'is_encrypted': 'isEncrypted',
            'value': 'value'
        }

        self._description = description
        self._is_encrypted = is_encrypted
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VariableCreateOrUpdateProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VariableCreateOrUpdateProperties of this VariableCreateOrUpdateProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this VariableCreateOrUpdateProperties.

        Gets or sets the description of the variable.

        :return: The description of this VariableCreateOrUpdateProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableCreateOrUpdateProperties.

        Gets or sets the description of the variable.

        :param description: The description of this VariableCreateOrUpdateProperties.
        :type description: str
        """

        self._description = description

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this VariableCreateOrUpdateProperties.

        Gets or sets the encrypted flag of the variable.

        :return: The is_encrypted of this VariableCreateOrUpdateProperties.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this VariableCreateOrUpdateProperties.

        Gets or sets the encrypted flag of the variable.

        :param is_encrypted: The is_encrypted of this VariableCreateOrUpdateProperties.
        :type is_encrypted: bool
        """

        self._is_encrypted = is_encrypted

    @property
    def value(self):
        """Gets the value of this VariableCreateOrUpdateProperties.

        Gets or sets the value of the variable.

        :return: The value of this VariableCreateOrUpdateProperties.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this VariableCreateOrUpdateProperties.

        Gets or sets the value of the variable.

        :param value: The value of this VariableCreateOrUpdateProperties.
        :type value: str
        """

        self._value = value
