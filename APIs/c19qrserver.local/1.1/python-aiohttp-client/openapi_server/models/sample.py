# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Sample(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, old_password: str=None, password: str=None):
        """Sample - a model defined in OpenAPI

        :param old_password: The old_password of this Sample.
        :param password: The password of this Sample.
        """
        self.openapi_types = {
            'old_password': str,
            'password': str
        }

        self.attribute_map = {
            'old_password': 'old_password',
            'password': 'password'
        }

        self._old_password = old_password
        self._password = password

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Sample':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Sample of this Sample.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def old_password(self):
        """Gets the old_password of this Sample.

        The old (current) password

        :return: The old_password of this Sample.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this Sample.

        The old (current) password

        :param old_password: The old_password of this Sample.
        :type old_password: str
        """

        self._old_password = old_password

    @property
    def password(self):
        """Gets the password of this Sample.

        The new password

        :return: The password of this Sample.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Sample.

        The new password

        :param password: The password of this Sample.
        :type password: str
        """

        self._password = password
