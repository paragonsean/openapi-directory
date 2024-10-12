# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.auth_confirm_identifier_type import AuthConfirmIdentifierType
from openapi_server import util


class AuthConfirmIdentifier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: AuthConfirmIdentifierType=None, value: str=None):
        """AuthConfirmIdentifier - a model defined in OpenAPI

        :param type: The type of this AuthConfirmIdentifier.
        :param value: The value of this AuthConfirmIdentifier.
        """
        self.openapi_types = {
            'type': AuthConfirmIdentifierType,
            'value': str
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuthConfirmIdentifier':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuthConfirmIdentifier of this AuthConfirmIdentifier.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this AuthConfirmIdentifier.


        :return: The type of this AuthConfirmIdentifier.
        :rtype: AuthConfirmIdentifierType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthConfirmIdentifier.


        :param type: The type of this AuthConfirmIdentifier.
        :type type: AuthConfirmIdentifierType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def value(self):
        """Gets the value of this AuthConfirmIdentifier.


        :return: The value of this AuthConfirmIdentifier.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AuthConfirmIdentifier.


        :param value: The value of this AuthConfirmIdentifier.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
