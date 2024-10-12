# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Argument(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_secret: bool=False, name: str=None, value: str=None):
        """Argument - a model defined in OpenAPI

        :param is_secret: The is_secret of this Argument.
        :param name: The name of this Argument.
        :param value: The value of this Argument.
        """
        self.openapi_types = {
            'is_secret': bool,
            'name': str,
            'value': str
        }

        self.attribute_map = {
            'is_secret': 'isSecret',
            'name': 'name',
            'value': 'value'
        }

        self._is_secret = is_secret
        self._name = name
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Argument':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Argument of this Argument.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_secret(self):
        """Gets the is_secret of this Argument.

        Flag to indicate whether the argument represents a secret and want to be removed from build logs.

        :return: The is_secret of this Argument.
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        """Sets the is_secret of this Argument.

        Flag to indicate whether the argument represents a secret and want to be removed from build logs.

        :param is_secret: The is_secret of this Argument.
        :type is_secret: bool
        """

        self._is_secret = is_secret

    @property
    def name(self):
        """Gets the name of this Argument.

        The name of the argument.

        :return: The name of this Argument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Argument.

        The name of the argument.

        :param name: The name of this Argument.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def value(self):
        """Gets the value of this Argument.

        The value of the argument.

        :return: The value of this Argument.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Argument.

        The value of the argument.

        :param value: The value of this Argument.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
