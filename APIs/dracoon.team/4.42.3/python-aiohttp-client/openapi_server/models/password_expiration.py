# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PasswordExpiration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None, max_password_age: int=None):
        """PasswordExpiration - a model defined in OpenAPI

        :param enabled: The enabled of this PasswordExpiration.
        :param max_password_age: The max_password_age of this PasswordExpiration.
        """
        self.openapi_types = {
            'enabled': bool,
            'max_password_age': int
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'max_password_age': 'maxPasswordAge'
        }

        self._enabled = enabled
        self._max_password_age = max_password_age

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PasswordExpiration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PasswordExpiration of this PasswordExpiration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this PasswordExpiration.

        Determines whether password expiration is enabled

        :return: The enabled of this PasswordExpiration.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PasswordExpiration.

        Determines whether password expiration is enabled

        :param enabled: The enabled of this PasswordExpiration.
        :type enabled: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def max_password_age(self):
        """Gets the max_password_age of this PasswordExpiration.

        Maximum allowed password age (in days)

        :return: The max_password_age of this PasswordExpiration.
        :rtype: int
        """
        return self._max_password_age

    @max_password_age.setter
    def max_password_age(self, max_password_age):
        """Sets the max_password_age of this PasswordExpiration.

        Maximum allowed password age (in days)

        :param max_password_age: The max_password_age of this PasswordExpiration.
        :type max_password_age: int
        """

        self._max_password_age = max_password_age
