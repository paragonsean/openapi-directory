# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RegistryInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location: str=None, password: str=None, user: str=None):
        """RegistryInfo - a model defined in OpenAPI

        :param location: The location of this RegistryInfo.
        :param password: The password of this RegistryInfo.
        :param user: The user of this RegistryInfo.
        """
        self.openapi_types = {
            'location': str,
            'password': str,
            'user': str
        }

        self.attribute_map = {
            'location': 'location',
            'password': 'password',
            'user': 'user'
        }

        self._location = location
        self._password = password
        self._user = user

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RegistryInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RegistryInfo of this RegistryInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self):
        """Gets the location of this RegistryInfo.

        The location.

        :return: The location of this RegistryInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RegistryInfo.

        The location.

        :param location: The location of this RegistryInfo.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")

        self._location = location

    @property
    def password(self):
        """Gets the password of this RegistryInfo.

        The password.

        :return: The password of this RegistryInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegistryInfo.

        The password.

        :param password: The password of this RegistryInfo.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def user(self):
        """Gets the user of this RegistryInfo.

        The user.

        :return: The user of this RegistryInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RegistryInfo.

        The user.

        :param user: The user of this RegistryInfo.
        :type user: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user
