# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildArgument(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_secret: bool=False, name: str=None, type: str=None, value: str=None):
        """BuildArgument - a model defined in OpenAPI

        :param is_secret: The is_secret of this BuildArgument.
        :param name: The name of this BuildArgument.
        :param type: The type of this BuildArgument.
        :param value: The value of this BuildArgument.
        """
        self.openapi_types = {
            'is_secret': bool,
            'name': str,
            'type': str,
            'value': str
        }

        self.attribute_map = {
            'is_secret': 'isSecret',
            'name': 'name',
            'type': 'type',
            'value': 'value'
        }

        self._is_secret = is_secret
        self._name = name
        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildArgument':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildArgument of this BuildArgument.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_secret(self):
        """Gets the is_secret of this BuildArgument.

        Flag to indicate whether the argument represents a secret and want to be removed from build logs.

        :return: The is_secret of this BuildArgument.
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        """Sets the is_secret of this BuildArgument.

        Flag to indicate whether the argument represents a secret and want to be removed from build logs.

        :param is_secret: The is_secret of this BuildArgument.
        :type is_secret: bool
        """

        self._is_secret = is_secret

    @property
    def name(self):
        """Gets the name of this BuildArgument.

        The name of the argument.

        :return: The name of this BuildArgument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildArgument.

        The name of the argument.

        :param name: The name of this BuildArgument.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """Gets the type of this BuildArgument.

        The type of the argument.

        :return: The type of this BuildArgument.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BuildArgument.

        The type of the argument.

        :param type: The type of this BuildArgument.
        :type type: str
        """
        allowed_values = ["DockerBuildArgument"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this BuildArgument.

        The value of the argument.

        :return: The value of this BuildArgument.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BuildArgument.

        The value of the argument.

        :param value: The value of this BuildArgument.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
